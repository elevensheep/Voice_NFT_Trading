from flask import Flask, request, send_file, jsonify
from transformers import AutoTokenizer
from datetime import datetime
import os
import torch
import soundfile as sf
import platform

from cli.SparkTTS import SparkTTS
from sparktts.utils.token_parser import LEVELS_MAP_UI

app = Flask(__name__)

if platform.system() == "Darwin":
    device = torch.device("mps:0")
elif torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")

print(f"디바이스 설정 완료: {device}")

model_dir = "pretrained_models/Spark-TTS-0.5B"
print("SparkTTS 모델 초기화 시작...")
try:
    model = SparkTTS(model_dir, device)
    print("SparkTTS 모델 초기화 성공")
except Exception as e:
    print(f"SparkTTS 모델 초기화 실패: {e}")
    exit(1)

SAVE_DIR = "example/results"
os.makedirs(SAVE_DIR, exist_ok=True)

def generate_tts(text, prompt_speech_path=None, gender=None, pitch=None, speed=None):
    with torch.no_grad():
        print("TTS 생성 시작...")
        wav = model.inference(
            text,
            prompt_speech_path,
            gender,
            pitch,
            speed
        )
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        save_path = os.path.join(SAVE_DIR, f"{timestamp}.wav")
        sf.write(save_path, wav, samplerate=16000)
        print(f"TTS 생성 완료: {save_path}")
        return save_path

@app.route("/voice-clone", methods=["POST"])
def voice_clone():
    print(" [POST] /voice-clone 요청 수신")
    text = request.form.get("text")
    prompt_speech = request.files.get("prompt_speech", None)

    prompt_path = None
    if prompt_speech:
        prompt_path = os.path.join(SAVE_DIR, f"prompt_{datetime.now().timestamp()}.wav")
        prompt_speech.save(prompt_path)
        print(f"프롬프트 음성 저장됨: {prompt_path}")

    output_path = generate_tts(text, prompt_speech_path=prompt_path)
    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    print("Flask 서버 시작 중...")
    app.run(host="0.0.0.0", port=5000)