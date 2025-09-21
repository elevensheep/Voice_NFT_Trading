@echo off
echo ========================================
echo 모든 서버 종료
echo ========================================

echo Node.js 프로세스 종료...
taskkill /f /im node.exe 2>nul

echo Python 프로세스 종료...
taskkill /f /im python.exe 2>nul

echo 모든 서버가 종료되었습니다.
pause
