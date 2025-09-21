# 🎙️ VoiceChain - 목소리 NFT 기반 AI 음성 플랫폼

> **목소리도 소유할 수 있습니다.**  
> VoiceChain은 사용자의 목소리를 NFT로 민팅하고, 인증된 음성을 AI TTS에 활용할 수 있도록 하는 Web3 기반 음성 자산화 플랫폼입니다.

[![Node.js](https://img.shields.io/badge/Node.js-16+-green)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🔥 핵심 기능

- **🔐 OAuth 소셜 로그인** - 카카오, 네이버 등 다양한 소셜 로그인 지원
- **🎤 AI 음성 클로닝** - SparkTTS 기반 고품질 음성 합성
- **🪙 NFT 민팅 및 거래** - 목소리를 NFT로 자산화
- **🏪 마켓플레이스** - NFT 거래 및 리셀 플랫폼
- **🌐 IPFS 기반 분산 저장** - 탈중앙화된 메타데이터 저장
- **📱 반응형 웹 인터페이스** - 모바일/데스크톱 최적화
- **📊 Swagger API 문서화** - 자동 생성된 API 문서

---

## 🧱 기술 스택

### Frontend
![React](https://img.shields.io/badge/React-61D9FB?style=for-the-badge&logo=React&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Backend
![Node.js](https://img.shields.io/badge/Node.js-16+-8FC708?style=for-the-badge&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-4.18-000000?style=for-the-badge&logo=express&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-7.6-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

### Blockchain
![Solidity](https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white)
![Truffle](https://img.shields.io/badge/Truffle-3C3C3C?style=for-the-badge&logo=truffle&logoColor=white)
![Web3](https://img.shields.io/badge/Web3-4.2-F16822?style=for-the-badge&logo=web3.js&logoColor=white)

### AI & TTS
![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.7-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![Flask-RESTX](https://img.shields.io/badge/Flask--RESTX-1.3-000000?style=for-the-badge&logo=flask&logoColor=white)

### Storage & Infrastructure
![IPFS](https://img.shields.io/badge/IPFS-65C2CB?style=for-the-badge&logo=ipfs&logoColor=white)
![Pinata](https://img.shields.io/badge/Pinata-4C4C4C?style=for-the-badge&logo=pinata&logoColor=white)

---

## 🏗️ 프로젝트 구조

```
Voice_NFT_Trading/
├── src/
│   ├── frontend/                    # React 프론트엔드
│   │   ├── src/
│   │   │   ├── components/         # UI 컴포넌트
│   │   │   ├── pages/             # 페이지 컴포넌트
│   │   │   ├── services/          # API 서비스
│   │   │   └── utils/             # 유틸리티
│   │   └── package.json
│   │
│   └── backend/
│       ├── node/                   # Node.js 백엔드
│       │   ├── auth/              # 인증 및 사용자 관리
│       │   ├── marketplace/       # NFT 마켓플레이스
│       │   │   ├── api/           # API 로직
│       │   │   ├── smart-contracts/ # 스마트 컨트랙트
│       │   │   └── frontend/      # NFT 민팅 프론트엔드
│       │   ├── voice/             # 음성 서비스
│       │   ├── config/            # 설정 관리
│       │   ├── middleware/        # 미들웨어
│       │   └── utils/             # 유틸리티
│       │
│       └── Spark-TTS-main/        # AI 음성 합성 서비스
│           ├── cli/               # CLI 도구
│           ├── sparktts/          # TTS 모델
│           ├── webui.py           # Flask 웹 서버 (Swagger 지원)
│           └── requirements.txt   # Python 의존성
│
├── docs/                          # 프로젝트 문서
├── .env.example                   # 환경변수 템플릿
└── README.md
```

---

## 🚀 빠른 시작

### 1. 저장소 클론
```bash
git clone https://github.com/elevensheep/Voice_NFT_Trading.git
cd Voice_NFT_Trading
```

### 2. 환경 설정
```bash
# 환경변수 파일 생성
cp .env.example .env

# 환경변수 설정 (필수)
# MongoDB URI, JWT Secret, OAuth 키 등 설정
```

### 3. 백엔드 서버 시작

#### Node.js 서버 (포트 8000)
```bash
cd src/backend/node
npm install
npm run dev
```

#### Python TTS 서버 (포트 5000)
```bash
cd src/backend/Spark-TTS-main
pip install -r requirements.txt
python webui.py
```

### 4. 프론트엔드 시작 (포트 3000)
```bash
cd src/frontend
npm install
npm start
```

### 5. 스마트 컨트랙트 배포
```bash
cd src/backend/node/marketplace/smart-contracts/truffle-project
npm install
npm run deploy
```

---

## 📋 주요 API 엔드포인트

### Node.js 백엔드 API (포트 8000)[Swagger UI](http://localhost:8000/api-docs)
#### 인증 (Authentication)
- `POST /api/auth/kakao` - 카카오 로그인
- `POST /api/auth/complete-profile` - 프로필 완성
- `GET /api/user/profile` - 사용자 정보 조회

#### 마켓플레이스 (Marketplace)
- `POST /api/marketplace/mint` - NFT 민팅
- `GET /api/marketplace/voiceList` - NFT 목록 조회
- `POST /api/marketplace/save` - NFT 메타데이터 저장

#### 음성 서비스 (Voice)
- `POST /api/voice/upload-voice` - 음성 프롬프트 업로드
- `POST /api/voice/generate-speech` - 음성 생성
- `GET /api/voice/voice-list` - 생성된 음성 목록

### Python TTS API (포트 5000) - [Swagger UI](http://localhost:5000/swagger/)
#### 음성 클로닝
- `POST /api/tts/upload-prompt` - 음성 프롬프트 업로드
- `POST /api/tts/voice-clone` - 텍스트를 음성으로 변환
- `POST /api/tts/voice-list` - 생성된 음성 목록 조회
- `GET /api/tts/results/<user_id>/<filename>` - 생성된 오디오 파일
- `GET /api/tts/health` - 서비스 상태 확인

---

## 🔧 개발 환경 설정

### 필수 요구사항
- **Node.js**: 16.0.0 이상
- **Python**: 3.9 이상
- **MongoDB**: 최신 버전
- **Git**: 버전 관리
---

## 📚 문서

### 🚀 시작하기
- [📖 전체 문서](docs/README.md) - 모든 문서의 중앙 허브
- [⚙️ 설치 가이드](docs/setup-guide.md) - 프로젝트 설치 및 환경 설정
- [🗄️ MongoDB 설정](docs/mongodb-setup.md) - 데이터베이스 설정 가이드
- [🎤 TTS 통합 가이드](docs/tts-integration-guide.md) - 음성 합성 서비스 연동

### 🏗️ 컴포넌트별 문서
- [🖥️ 백엔드 서버](docs/components/backend.md) - Node.js API 서버
- [🌐 프론트엔드](docs/components/frontend.md) - React 웹 애플리케이션
- [🎵 TTS 서비스](docs/components/tts-service.md) - SparkTTS 음성 합성
- [⛓️ 스마트 컨트랙트](docs/components/smart-contracts.md) - 블록체인 컨트랙트

### 📁 프로젝트 구조
- [📂 폴더 구조 가이드](docs/folder-structure.md) - 프로젝트 구조 이해

---

## 🐛 문제 해결

### 자주 발생하는 문제들

#### 1. Node.js 16 호환성 문제
```bash
# 해결 방법
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

#### 2. Python TTS 서비스 오류
```bash
# 가상환경 활성화
cd src/backend/Spark-TTS-main
source venv39/bin/activate  # Linux/Mac
# 또는
venv39\Scripts\activate     # Windows

# 의존성 재설치
pip install -r requirements.txt
```

#### 3. MongoDB 연결 오류
- MongoDB 서비스가 실행 중인지 확인
- MONGO_URI 환경변수 설정 확인
- 방화벽 및 포트 설정 확인



<div align="center">
**🔗 관련 링크**
- [SparkTTS 모델](https://huggingface.co/SparkAudio/Spark-TTS-0.5B)
- [프로젝트 이슈](https://github.com/elevensheep/Voice_NFT_Trading/issues)
</div>