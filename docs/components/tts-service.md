# Spark-TTS Service

경량화된 Spark-TTS 음성 클로닝 서비스입니다.

## 🚀 빠른 시작

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 모델 다운로드
```bash
python download_model.py
```

### 3. 서버 시작
```bash
# Linux/Mac
./start_servers.sh

# Windows
python webui.py
```

## 📁 폴더 구조

```
Spark-TTS-main/
├── cli/                    # CLI 도구
│   ├── SparkTTS.py        # 메인 TTS 클래스
│   └── inference.py       # 추론 스크립트
├── sparktts/              # TTS 모델 코드
│   ├── models/            # 모델 정의
│   ├── modules/           # 모듈들
│   └── utils/             # 유틸리티
├── webui.py              # Flask 웹 서버
├── start_servers.sh      # 시작 스크립트
├── requirements.txt      # 의존성
└── README.md            # 이 파일
```

## 🔧 API 엔드포인트

### POST /upload-prompt
음성 프롬프트 업로드
- `user_id`: 사용자 ID
- `prompt_speech`: 음성 파일

### POST /voice-clone
음성 클로닝 생성
- `user_id`: 사용자 ID
- `text`: 변환할 텍스트

### POST /voice-list
생성된 음성 목록 조회
- `user_id`: 사용자 ID

### GET /health
서버 상태 확인

## ⚙️ 설정

- **포트**: 5000
- **디바이스**: 자동 감지 (CUDA/MPS/CPU)
- **샘플링 레이트**: 16kHz
- **오디오 포맷**: WAV

## 📝 사용법

1. 음성 프롬프트 업로드
2. 텍스트 입력하여 음성 생성
3. 생성된 음성 파일 다운로드

## 🔧 최적화 사항

- 불필요한 파일 제거
- 가상환경 제거
- Docker 관련 파일 제거
- 중복 의존성 정리
- 코드 간소화
