# 📚 VoiceChain 문서

VoiceChain 프로젝트의 모든 문서를 한 곳에서 확인할 수 있습니다.

## 🚀 시작하기

### 설치 및 설정
- [설치 가이드](setup-guide.md) - 프로젝트 설치 및 환경 설정
- [MongoDB 설정](mongodb-setup.md) - 데이터베이스 설정 가이드
- [TTS 통합 가이드](tts-integration-guide.md) - 음성 합성 서비스 연동
- [폴더 구조 가이드](folder-structure.md) - 프로젝트 구조 이해

## 🏗️ 컴포넌트별 문서

### 백엔드 서버
- [백엔드 서버](components/backend.md) - Node.js API 서버 상세 가이드
- [스마트 컨트랙트](components/smart-contracts.md) - 블록체인 컨트랙트 개발

### 프론트엔드
- [프론트엔드](components/frontend.md) - React 웹 애플리케이션 가이드

### AI & TTS 서비스
- [TTS 서비스](components/tts-service.md) - SparkTTS 음성 합성 서비스

## 📋 API 문서

### Node.js 백엔드 API
- **인증**: `/api/auth/*` - 사용자 인증 및 프로필 관리
- **마켓플레이스**: `/api/marketplace/*` - NFT 거래 및 관리
- **음성 서비스**: `/api/voice/*` - 음성 클로닝 및 TTS
- **사용자 관리**: `/api/user/*` - 사용자 정보 관리

### Python TTS API (Swagger UI: http://localhost:5000/swagger/)
- **음성 업로드**: `POST /api/tts/upload-prompt` - 음성 프롬프트 업로드
- **음성 생성**: `POST /api/tts/voice-clone` - 텍스트를 음성으로 변환
- **음성 목록**: `POST /api/tts/voice-list` - 생성된 음성 목록 조회
- **오디오 제공**: `GET /api/tts/results/<user_id>/<filename>` - 생성된 오디오 파일
- **헬스체크**: `GET /api/tts/health` - 서비스 상태 확인

## 🔧 개발 가이드

### 환경 요구사항
- **Node.js**: 16.0.0 이상
- **Python**: 3.9 이상
- **MongoDB**: 최신 버전
- **Git**: 버전 관리

### 코드 스타일
- **JavaScript**: ES6+ 문법 사용
- **React**: 함수형 컴포넌트 및 Hooks 사용
- **Node.js**: Express.js 기반 RESTful API
- **Python**: PEP 8 스타일 가이드 준수

### 폴더 구조 원칙
- **단일 책임 원칙**: 각 폴더는 명확한 하나의 기능 담당
- **관심사 분리**: API, 스마트 컨트랙트, 프론트엔드 분리
- **확장성**: 새로운 기능 추가 시 기존 구조 유지

## 🐛 문제 해결

### 자주 묻는 질문

#### 1. 서버 시작 오류
- **포트 충돌**: 8000(Node.js), 5000(Python TTS) 포트 확인
- **환경변수**: `.env` 파일 설정 확인
- **의존성**: `npm install` 및 `pip install -r requirements.txt` 실행

#### 2. TTS 서비스 연결 실패
- **Python 환경**: venv39 가상환경 활성화 확인
- **모델 다운로드**: Spark-TTS 모델 파일 존재 확인
- **Flask-RESTX**: `pip install flask-restx` 설치 확인

#### 3. 데이터베이스 연결 오류
- **MongoDB 서버**: MongoDB 서비스 실행 상태 확인
- **연결 URI**: MONGO_URI 환경변수 설정 확인
- **네트워크**: 방화벽 및 포트 설정 확인

#### 4. Node.js 16 호환성 문제
- **패키지 버전**: package.json의 호환 버전 확인
- **npm 캐시**: `npm cache clean --force` 실행
- **node_modules**: 삭제 후 재설치

### 로그 확인
- **백엔드**: `src/backend/node/` 디렉토리에서 서버 로그 확인
- **TTS 서비스**: `src/backend/Spark-TTS-main/` 디렉토리에서 Flask 로그 확인
- **프론트엔드**: 브라우저 개발자 도구 콘솔 확인

## 📊 프로젝트 현황

### 완료된 기능
- ✅ OAuth 소셜 로그인 (카카오)
- ✅ 음성 클로닝 및 TTS
- ✅ NFT 민팅 및 거래
- ✅ 마켓플레이스 플랫폼
- ✅ IPFS 기반 분산 저장
- ✅ Swagger API 문서화

### 개발 중인 기능
- 🔄 다중 소셜 로그인 지원
- 🔄 고급 음성 조절 기능
- 🔄 실시간 NFT 거래
- 🔄 모바일 앱 지원

## 📞 지원

- **GitHub Issues**: [프로젝트 이슈](https://github.com/elevensheep/Voice_NFT_Trading/issues)
- **문서 개선**: [Pull Request](https://github.com/elevensheep/Voice_NFT_Trading/pulls) 제출
- **기술 지원**: 개발팀 문의

---

> 💡 **팁**: 특정 컴포넌트에 대한 자세한 정보는 해당 컴포넌트의 문서를 참조하세요.

> 🔗 **링크**: [메인 README](../README.md)로 돌아가기