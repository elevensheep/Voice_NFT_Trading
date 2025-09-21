# Smart Contracts

Voice NFT Trading Platform의 스마트 컨트랙트 관련 파일들입니다.

## 📁 구조

```
smart-contracts/
├── truffle-project/        # Truffle 프로젝트
│   ├── contracts/         # 스마트 컨트랙트 소스
│   ├── migrations/        # 배포 스크립트
│   ├── scripts/          # 커스텀 스크립트
│   └── test/             # 테스트 파일
└── scripts/              # 배포 및 유틸리티 스크립트
    └── deploy-contract.js # 컨트랙트 배포 스크립트
```

## 🚀 사용법

### 1. 의존성 설치
```bash
cd truffle-project
npm install
```

### 2. 컨트랙트 배포
```bash
# 자동 배포 (컴파일 + 배포 + ABI 복사)
npm run deploy

# 또는 수동으로
npm run migrate
```

### 3. 개별 명령어
```bash
npm run compile  # 컴파일만
npm run test     # 테스트 실행
```

## 📋 스크립트 설명

### `deploy-contract.js`
- 스마트 컨트랙트 컴파일 및 배포
- ABI 파일을 프론트엔드로 자동 복사
- 배포 상태 로깅

## 🔧 설정

- **네트워크**: `truffle-config.js`에서 설정
- **컴파일러**: Solidity 0.8.30
- **프레임워크**: Truffle
- **라이브러리**: OpenZeppelin Contracts

## 📝 주의사항

- 배포 전에 네트워크 설정을 확인하세요
- 프라이빗 키는 환경변수로 관리하세요
- 테스트넷에서 먼저 테스트하세요
