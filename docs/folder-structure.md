# 폴더 구조 가이드

이 문서는 리팩토링된 백엔드 폴더 구조를 설명합니다.

## 📁 새로운 폴더 구조

```
node/
├── config/                 # 설정 관리
│   └── index.js           # 중앙화된 설정
├── middleware/            # 미들웨어
│   ├── auth.js           # 인증 미들웨어
│   ├── errorHandler.js   # 에러 핸들링
│   └── validation.js     # 입력 검증
├── auth/                  # 인증 및 사용자 관리
│   ├── controllers/      # 인증 컨트롤러
│   ├── models/          # 사용자 모델
│   ├── routes/          # 인증 라우트
│   ├── services/        # OAuth 서비스
│   └── utils/           # JWT 유틸리티
├── marketplace/          # NFT 마켓플레이스
│   ├── api/             # API 로직
│   │   ├── controllers/ # NFT 컨트롤러
│   │   ├── models/     # NFT 모델
│   │   ├── routes/     # NFT 라우트
│   │   └── services/   # NFT 서비스
│   ├── smart-contracts/ # 스마트 컨트랙트
│   │   └── truffle-project/
│   └── frontend/        # NFT 민팅 프론트엔드
├── voice/               # 음성 서비스
│   ├── controllers/    # TTS 컨트롤러
│   ├── routes/        # TTS 라우트
│   └── services/      # TTS 서비스
├── utils/              # 유틸리티
│   ├── db.js          # 데이터베이스 연결
│   └── swagger.js     # API 문서
├── server.js          # 메인 서버
└── package.json       # 의존성 관리
```

## 🔄 폴더 이름 변경 사항

| 이전 이름 | 새 이름 | 이유 |
|-----------|---------|------|
| `oauth/` | `auth/` | OAuth뿐만 아니라 전체 인증 및 사용자 관리 기능을 포함 |
| `NFT/` | `marketplace/` | NFT 민팅, 거래, 마켓플레이스 기능을 모두 포함 |
| `tts/` | `voice/` | TTS뿐만 아니라 음성 클로닝, 음성 서비스 전체를 포함 |

## 📋 각 폴더의 역할

### 🔐 auth/ - 인증 및 사용자 관리
- **목적**: 사용자 인증, OAuth 처리, 프로필 관리
- **주요 기능**:
  - 카카오 OAuth 로그인
  - JWT 토큰 관리
  - 사용자 프로필 완성
  - 지갑 주소 연결

### 🏪 marketplace/ - NFT 마켓플레이스
- **목적**: NFT 생성, 거래, 마켓플레이스 운영
- **주요 기능**:
  - NFT 민팅 (스마트 컨트랙트)
  - NFT 거래 기록
  - 마켓플레이스 API
  - NFT 프론트엔드

### 🎤 voice/ - 음성 서비스
- **목적**: 음성 클로닝, TTS 생성, 음성 관련 서비스
- **주요 기능**:
  - 음성 파일 업로드
  - 음성 모델 학습
  - TTS 음성 생성
  - 음성 상태 확인

## 🚀 API 엔드포인트 변경

| 이전 경로 | 새 경로 | 설명 |
|-----------|---------|------|
| `/api/auth/*` | `/api/auth/*` | 인증 관련 (변경 없음) |
| `/api/nft/*` | `/api/marketplace/*` | NFT 마켓플레이스 |
| `/api/user/*` | `/api/user/*` | 사용자 관리 (변경 없음) |
| `/api/tts/*` | `/api/voice/*` | 음성 서비스 |

## 📝 마이그레이션 가이드

### 1. 서버 재시작
```bash
npm run dev
```

### 2. API 호출 업데이트
- NFT 관련 API: `/api/nft/*` → `/api/marketplace/*`
- TTS 관련 API: `/api/tts/*` → `/api/voice/*`

### 3. 프론트엔드 업데이트
- API 엔드포인트 URL 변경
- 새로운 폴더 구조에 맞는 import 경로 수정

## 🔧 개발 가이드

### 새로운 기능 추가 시
1. **인증 관련**: `auth/` 폴더에 추가
2. **NFT/마켓플레이스 관련**: `marketplace/api/` 폴더에 추가
3. **음성 관련**: `voice/` 폴더에 추가

### 폴더 구조 원칙
- **단일 책임 원칙**: 각 폴더는 명확한 하나의 기능을 담당
- **관심사 분리**: API, 스마트 컨트랙트, 프론트엔드를 분리
- **확장성**: 새로운 기능 추가 시 기존 구조를 유지하면서 확장 가능
