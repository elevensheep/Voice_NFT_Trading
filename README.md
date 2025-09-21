# 🎙️ VoiceChain - 목소리 NFT 기반 AI 음성 플랫폼

> **목소리도 소유할 수 있습니다.**  
> VoiceChain은 사용자의 목소리를 NFT로 민팅하고, 인증된 음성을 AI TTS에 활용할 수 있도록 하는 Web3 기반 음성 자산화 플랫폼입니다.

---

## 🔥 핵심 기능

- **🔐 OAuth 소셜 로그인** - 카카오, 네이버 등 다양한 소셜 로그인 지원
- **🎤 AI 음성 클로닝** - SparkTTS 기반 고품질 음성 합성
- **🪙 NFT 민팅 및 거래** - 목소리를 NFT로 자산화
- **🏪 마켓플레이스** - NFT 거래 및 리셀 플랫폼
- **🌐 IPFS 기반 분산 저장** - 탈중앙화된 메타데이터 저장
- **📱 반응형 웹 인터페이스** - 모바일/데스크톱 최적화

---

## 🧱 기술 스택

### Frontend
![React](https://img.shields.io/badge/React-61D9FB?style=for-the-badge&logo=React&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Backend
![Node.js](https://img.shields.io/badge/Node.js-8FC708?style=for-the-badge&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)

### Blockchain
![Solidity](https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white)
![Truffle](https://img.shields.io/badge/Truffle-3C3C3C?style=for-the-badge&logo=truffle&logoColor=white)
![Web3](https://img.shields.io/badge/Web3-F16822?style=for-the-badge&logo=web3.js&logoColor=white)

### AI & TTS
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

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
│           └── webui.py           # Flask 웹 서버
│
├── docs/                          # 프로젝트 문서
├── .github/                       # GitHub Actions
└── README.md
```

---

## 🚀 빠른 시작

### 1. 저장소 클론
```bash
git clone https://github.com/your-username/Voice_NFT_Trading.git
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

#### Node.js 서버
```bash
cd src/backend/node
npm install
npm run dev
```

#### TTS 서버
```bash
cd src/backend/Spark-TTS-main
pip install -r requirements.txt
python webui.py
```

### 4. 프론트엔드 시작
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

### 인증 (Authentication)
- `POST /api/auth/kakao` - 카카오 로그인
- `POST /api/auth/complete-profile` - 프로필 완성
- `GET /api/user/profile` - 사용자 정보 조회

### 마켓플레이스 (Marketplace)
- `POST /api/marketplace/mint` - NFT 민팅
- `GET /api/marketplace/voiceList` - NFT 목록 조회
- `POST /api/marketplace/save` - NFT 메타데이터 저장

### 음성 서비스 (Voice)
- `POST /api/voice/upload-voice` - 음성 프롬프트 업로드
- `POST /api/voice/generate-speech` - 음성 생성
- `GET /api/voice/voice-list` - 생성된 음성 목록

---

## 🔧 개발 환경 설정

### 필수 요구사항
- Node.js 16+
- Python 3.9+
- MongoDB
- Git

### 환경변수 설정
```env
# 서버 설정
PORT=8000
NODE_ENV=development
FRONTEND_URL=http://localhost:3000

# 데이터베이스
MONGO_URI=mongodb://localhost:27017/voice-nft

# JWT
JWT_SECRET=your-secret-key
JWT_EXPIRES_IN=7d

# OAuth (카카오)
KAKAO_CLIENT_ID=your-kakao-client-id
KAKAO_CLIENT_SECRET=your-kakao-client-secret
KAKAO_REDIRECT_URI=http://localhost:8000/api/auth/kakao/callback

# TTS 서버
FLASK_TTS_URL=http://localhost:5000
```

---

## 📚 문서

### 🚀 시작하기
- [설치 가이드](docs/setup-guide.md)
- [MongoDB 설정](docs/mongodb-setup.md)
- [TTS 통합 가이드](docs/tts-integration-guide.md)

### 🏗️ 컴포넌트별 문서
- [백엔드 서버](docs/components/backend.md) - Node.js API 서버
- [프론트엔드](docs/components/frontend.md) - React 웹 애플리케이션
- [TTS 서비스](docs/components/tts-service.md) - SparkTTS 음성 합성
- [스마트 컨트랙트](docs/components/smart-contracts.md) - 블록체인 컨트랙트

### 📁 프로젝트 구조
- [폴더 구조 가이드](docs/folder-structure.md)

---

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## 👥 팀

- **개발팀** - VoiceChain Development Team
- **AI 연구팀** - SparkTTS Integration Team
- **블록체인팀** - Smart Contract Development Team

---



---

<div align="center">

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요! ⭐**
https://huggingface.co/SparkAudio/Spark-TTS-0.5B/tree/
main
</div>