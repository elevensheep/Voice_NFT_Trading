@echo off
echo ========================================
echo Node.js 서버 시작
echo ========================================

echo Node.js 16 버전으로 전환...
call nvm use 16.20.2

echo Node.js 서버 시작 (포트 8000)...
cd src\backend\node
npm start

pause
