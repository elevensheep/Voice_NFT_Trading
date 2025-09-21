from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields, Namespace
import os
import torch
import soundfile as sf
import platform
from pydub import AudioSegment
import tempfile
from datetime import datetime

from cli.SparkTTS import SparkTTS

app = Flask(__name__)
CORS(app)

# Swagger API 설정
api = Api(
    app, 
    version='1.0', 
    title='Voice NFT Trading Platform - TTS API',
    description='Text-to-Speech API for Voice NFT Trading Platform',
    doc='/swagger/',
    prefix='/api'
)

# 네임스페이스 생성
ns = api.namespace('tts', description='Text-to-Speech operations')

# API 모델 정의
upload_model = api.model('UploadPrompt', {
    'user_id': fields.String(required=True, description='User ID for voice cloning'),
    'prompt_speech': fields.Raw(required=True, description='Audio file for voice prompt')
})

voice_clone_model = api.model('VoiceClone', {
    'user_id': fields.String(required=True, description='User ID'),
    'text': fields.String(required=True, description='Text to convert to speech')
})

voice_list_model = api.model('VoiceList', {
    'user_id': fields.String(required=True, description='User ID to get voice list for')
})

response_model = api.model('Response', {
    'message': fields.String(description='Response message'),
    'error': fields.String(description='Error message')
})

voice_list_response = api.model('VoiceListResponse', {
    'voices': fields.List(fields.String, description='List of voice file URLs')
})

# Device configuration
if platform.system() == "Darwin":
    device = torch.device("mps:0")
elif torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")

print(f"Device: {device}")

# Model initialization
model_dir = "pretrained_models/Spark-TTS-0.5B"
print("Initializing SparkTTS model...")
try:
    model = SparkTTS(model_dir, device)
    print("SparkTTS model initialized successfully")
except Exception as e:
    print(f"Failed to initialize SparkTTS model: {e}")
    exit(1)

# Directory setup
SAVE_DIR = "results"
PROMPT_DIR = "prompts"
os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(PROMPT_DIR, exist_ok=True)

def generate_tts(user_id, text, gender=None, pitch=None, speed=None):
    """Generate TTS audio for given user and text"""
    prompt_path = os.path.join(PROMPT_DIR, f"{user_id}.wav")
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt audio for user ID `{user_id}` not found")

    with torch.no_grad():
        print(f"Generating TTS... [user_id: {user_id}]")
        wav = model.inference(text, prompt_path, gender, pitch, speed)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        user_dir = os.path.join(SAVE_DIR, user_id)
        os.makedirs(user_dir, exist_ok=True)
        save_path = os.path.join(user_dir, f"{timestamp}.wav")
        sf.write(save_path, wav, samplerate=16000)
        print(f"TTS generation completed: {save_path}")
        return save_path

@ns.route('/upload-prompt')
class UploadPrompt(Resource):
    @ns.expect(upload_model)
    @ns.marshal_with(response_model)
    def post(self):
        """Upload and process prompt audio for voice cloning"""
        user_id = request.form.get("user_id")
        prompt_speech = request.files.get("prompt_speech")

        if not user_id or not prompt_speech:
            return {"error": "user_id and prompt_speech are required"}, 400

        prompt_path = os.path.join(PROMPT_DIR, f"{user_id}.wav")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as tmp:
            tmp_path = tmp.name
            prompt_speech.save(tmp_path)

        # Convert to required format
        audio = AudioSegment.from_file(tmp_path)
        audio = audio.set_channels(1).set_frame_rate(16000)
        audio.export(prompt_path, format="wav", codec="pcm_s16le")

        os.remove(tmp_path)
        print(f"[{user_id}] Prompt saved and converted: {prompt_path}")
        return {"message": "Prompt audio saved successfully"}

@ns.route('/voice-clone')
class VoiceClone(Resource):
    @ns.expect(voice_clone_model)
    def post(self):
        """Generate voice clone from text"""
        user_id = request.form.get("user_id")
        text = request.form.get("text")

        if not user_id or not text:
            return {"error": "user_id and text are required"}, 400

        try:
            output_path = generate_tts(user_id, text)
            filename = os.path.basename(output_path)

            response = send_file(
                output_path,
                mimetype="audio/wav",
                as_attachment=True,
                download_name=filename
            )
            
            response.headers['X-Filename'] = filename
            response.headers['X-Filepath'] = output_path
            
            return response

        except FileNotFoundError as e:
            return {"error": str(e)}, 404

@ns.route('/results/<user_id>/<filename>')
class ServeAudio(Resource):
    def get(self, user_id, filename):
        """Serve generated audio files"""
        path = os.path.join(SAVE_DIR, user_id)
        return send_file(os.path.join(path, filename))

@ns.route('/voice-list')
class VoiceList(Resource):
    @ns.expect(voice_list_model)
    @ns.marshal_with(voice_list_response)
    def post(self):
        """Get list of generated voices for a user"""
        data = request.get_json()
        user_id = data.get("user_id")

        if not user_id:
            return {"error": "user_id is required"}, 400

        user_dir = os.path.join(SAVE_DIR, user_id)

        if not os.path.exists(user_dir):
            return {"voices": []}

        files = sorted(
            [f for f in os.listdir(user_dir) if f.endswith(".wav")],
            reverse=True
        )

        file_urls = [f"/api/tts/results/{user_id}/{f}" for f in files]
        return {"voices": file_urls}

@ns.route('/health')
class HealthCheck(Resource):
    def get(self):
        """Health check endpoint"""
        return {"status": "healthy", "device": str(device)}

if __name__ == "__main__":
    print("Starting Flask server...")
    print("=" * 50)
    print("🚀 Voice NFT Trading Platform - TTS API")
    print("=" * 50)
    print(f"📊 Swagger UI: http://localhost:5000/swagger/")
    print(f"🔧 API Base: http://localhost:5000/api/")
    print(f"💻 Device: {device}")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=False)