# Voice NFT 백엔드

Voice NFT 거래 플랫폼의 백엔드 서버로, Node.js, Express, MongoDB로 구축되었습니다.

## 🏗️ 프로젝트 구조

```
node/
├── config/                 # 설정 관리
│   └── index.js           # 중앙화된 설정
├── middleware/            # 커스텀 미들웨어
│   ├── auth.js           # 인증 미들웨어
│   ├── errorHandler.js   # 전역 에러 핸들링
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
│   └── frontend/        # NFT 민팅 프론트엔드
├── voice/               # 음성 서비스
│   ├── controllers/    # 음성 컨트롤러
│   ├── routes/        # 음성 라우트
│   └── services/      # 음성 서비스
├── utils/              # 유틸리티 함수
│   ├── db.js          # 데이터베이스 연결
│   └── swagger.js     # API 문서
├── server.js          # 메인 서버 파일
└── package.json       # 의존성 및 스크립트
```

## 🚀 시작하기

### 전제 조건

- Node.js (v16 이상)
- MongoDB
- npm 또는 yarn

### 설치

1. 의존성 설치:
```bash
npm install
```

2. 루트 디렉토리에 `.env` 파일 생성:
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
```

3. 서버 시작:
```bash
# 개발 환경
npm run dev

# 프로덕션
npm start
```

## 📚 API 문서

서버가 실행되면 다음 주소에서 API 문서에 접근할 수 있습니다:
- Swagger UI: `http://localhost:8000/api-docs`
- 헬스 체크: `http://localhost:8000/health`

### API 엔드포인트

- **인증**: `/api/auth/*` - 사용자 로그인, OAuth, 프로필 관리
- **마켓플레이스**: `/api/marketplace/*` - NFT 민팅, 거래, 마켓플레이스
- **사용자 관리**: `/api/user/*` - 사용자 프로필, 설정
- **음성 서비스**: `/api/voice/*` - TTS 생성, 음성 클로닝

## 🔧 설정

모든 설정은 `config/index.js`에서 중앙화되어 관리됩니다. 설정에는 다음이 포함됩니다:

- 서버 설정 (포트, 환경)
- 데이터베이스 연결 설정
- JWT 설정
- OAuth 제공자 설정
- CORS 설정
- 파일 업로드 설정

## 🛡️ 보안 기능

- JWT 기반 인증
- express-validator를 사용한 입력 검증
- CORS 보호
- 에러 핸들링 미들웨어
- 우아한 종료 처리

## 📝 사용 가능한 스크립트

- `npm start` - 프로덕션 서버 시작
- `npm run dev` - nodemon으로 개발 서버 시작
- `npm test` - 테스트 실행 (플레이스홀더)
- `npm run lint` - 린팅 실행 (플레이스홀더)

## 🔄 리팩토링 개선사항

이 리팩토링된 버전에는 다음이 포함됩니다:

1. **중앙화된 설정**: 모든 환경 변수와 설정을 한 곳에서 관리
2. **향상된 에러 핸들링**: 특정 에러 타입에 대한 전역 에러 핸들러
3. **개선된 데이터베이스 연결**: 적절한 에러 핸들링이 있는 연결 클래스
4. **미들웨어 구성**: 논리적 모듈로 미들웨어 분리
5. **입력 검증**: 요청 검증을 위한 express-validator 통합
6. **우아한 종료**: 서버 종료 시 적절한 정리 작업
7. **헬스 체크**: 서버 상태 모니터링 엔드포인트
8. **코드 구성**: 더 나은 파일 구조와 관심사 분리

## 🐛 에러 핸들링

애플리케이션에는 다음에 대한 포괄적인 에러 핸들링이 포함되어 있습니다:

- Mongoose 검증 에러
- 중복 키 에러
- JWT 토큰 에러
- 캐스트 에러 (잘못된 ObjectId)
- 일반 서버 에러

모든 에러는 일관된 JSON 응답 형식을 반환합니다:

```json
{
  "success": false,
  "message": "에러 설명",
  "errors": ["상세한 에러 메시지"]
}
```

## 🔐 인증

애플리케이션은 인증을 위해 JWT 토큰을 사용합니다. 보호된 라우트는 `authenticateToken` 미들웨어를 사용해야 합니다:

```javascript
const { authenticateToken } = require('./middleware/auth');

router.get('/protected', authenticateToken, (req, res) => {
  // req.user를 통해 사용자 정보에 접근
});
```