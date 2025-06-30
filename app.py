from flask import Flask, request, send_file, jsonify
import os
import torch
import soundfile as sf
import platform
from datetime import datetime
from cli.SparkTTS import SparkTTS
from sparktts.utils.token_parser import LEVELS_MAP_UI

app = Flask(__name__)

if platform.system() == "Darwin":
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
    torch.backends.mps.is_available = lambda: False
    device = torch.device("cpu")
elif torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")

model = SparkTTS("pretrained_models/Spark-TTS-0.5B", device)

OUTPUT_DIR = "example/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def synthesize_audio(text, prompt_speech=None, prompt_text=None, gender=None, pitch=None, speed=None):
    if prompt_speech is None:
        prompt_speech = os.path.abspath("example/prompt_audio.wav")
    if prompt_text is None:
        prompt_text = "안녕하세요"

    with torch.no_grad():
        wav = model.inference(text, prompt_speech, prompt_text, gender, pitch, speed)
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"
        save_path = os.path.join("example/results", filename)
        sf.write(save_path, wav, samplerate=16000)
        return save_path

@app.route("/synthesize", methods=["POST"])
def synthesize():
    data = request.json
    text = data.get("text")
    gender = data.get("gender", None)
    pitch = LEVELS_MAP_UI.get(int(data.get("pitch", 3)), None)
    speed = LEVELS_MAP_UI.get(int(data.get("speed", 3)), None)

    if not text:
        return jsonify({"error": "Text is required"}), 400

    prompt_speech = os.path.abspath("example/prompt_audio.wav")
    prompt_text = "안녕하세요"  

    audio_path = synthesize_audio(
        text,
        prompt_speech=prompt_speech,
        prompt_text=prompt_text,
        gender=gender,
        pitch=pitch,
        speed=speed
    )

    return send_file(audio_path, mimetype="audio/wav")

@app.route("/clone", methods=["POST"])
def clone():
    text = request.form.get("text")
    prompt_text = request.form.get("prompt_text")
    prompt_file = request.files.get("prompt_speech")

    if not text or not prompt_file:
        return jsonify({"error": "Text and prompt_speech are required"}), 400

    prompt_path = os.path.join(OUTPUT_DIR, "uploaded_prompt.wav")
    prompt_file.save(prompt_path)

    audio_path = synthesize_audio(text, prompt_speech=prompt_path, prompt_text=prompt_text)
    return send_file(audio_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)