# 📚 VoiceChain 문서

VoiceChain 프로젝트의 모든 문서를 한 곳에서 확인할 수 있습니다.

## 🚀 시작하기

### 설치 및 설정
- [설치 가이드](setup-guide.md) - 프로젝트 설치 및 환경 설정
- [MongoDB 설정](mongodb-setup.md) - 데이터베이스 설정 가이드
- [TTS 통합 가이드](tts-integration-guide.md) - 음성 합성 서비스 연동

## 🏗️ 컴포넌트별 문서

### 백엔드
- [백엔드 서버](components/backend.md) - Node.js API 서버 상세 가이드
- [폴더 구조 가이드](folder-structure.md) - 백엔드 코드 구조

### 프론트엔드
- [프론트엔드](components/frontend.md) - React 웹 애플리케이션 가이드

### AI & TTS
- [TTS 서비스](components/tts-service.md) - SparkTTS 음성 합성 서비스

### 블록체인
- [스마트 컨트랙트](components/smart-contracts.md) - 블록체인 컨트랙트 개발

## 📋 API 문서

### 백엔드 API
- **인증**: `/api/auth/*` - 사용자 인증 및 프로필 관리
- **마켓플레이스**: `/api/marketplace/*` - NFT 거래 및 관리
- **음성 서비스**: `/api/voice/*` - 음성 클로닝 및 TTS
- **사용자 관리**: `/api/user/*` - 사용자 정보 관리

### TTS API
- **음성 업로드**: `POST /upload-prompt` - 음성 프롬프트 업로드
- **음성 생성**: `POST /voice-clone` - 텍스트를 음성으로 변환
- **음성 목록**: `POST /voice-list` - 생성된 음성 목록 조회

## 🔧 개발 가이드

### 코드 스타일
- **JavaScript**: ES6+ 문법 사용
- **React**: 함수형 컴포넌트 및 Hooks 사용
- **Node.js**: Express.js 기반 RESTful API

### 폴더 구조 원칙
- **단일 책임 원칙**: 각 폴더는 명확한 하나의 기능 담당
- **관심사 분리**: API, 스마트 컨트랙트, 프론트엔드 분리
- **확장성**: 새로운 기능 추가 시 기존 구조 유지

## 🐛 문제 해결

### 자주 묻는 질문
1. **서버 시작 오류**: 포트 충돌 확인 및 환경변수 설정
2. **TTS 서비스 연결 실패**: Python 환경 및 모델 다운로드 확인
3. **데이터베이스 연결 오류**: MongoDB 서버 상태 및 URI 확인

### 로그 확인
- **백엔드**: `src/backend/node/` 디렉토리에서 서버 로그 확인
- **TTS 서비스**: `src/backend/Spark-TTS-main/` 디렉토리에서 Flask 로그 확인

## 📞 지원

- **GitHub Issues**: [프로젝트 이슈](https://github.com/your-username/Voice_NFT_Trading/issues)
- **문서 개선**: [Pull Request](https://github.com/your-username/Voice_NFT_Trading/pulls) 제출

---

> 💡 **팁**: 특정 컴포넌트에 대한 자세한 정보는 해당 컴포넌트의 README를 참조하세요.
