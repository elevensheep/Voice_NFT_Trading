# Voice NFT Trading Platform 시작 스크립트
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Voice NFT Trading Platform 시작" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Node.js 16 버전으로 전환
Write-Host "`n[1/4] Node.js 16 버전으로 전환..." -ForegroundColor Yellow
try {
    nvm use 16.20.2
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Node.js 16 버전 전환 실패" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
} catch {
    Write-Host "nvm 명령을 찾을 수 없습니다. Node.js 16이 설치되어 있는지 확인하세요." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Python 가상환경 설정
Write-Host "`n[2/4] Python 가상환경 설정..." -ForegroundColor Yellow
if (Test-Path "venv39\Scripts\Activate.ps1") {
    & "venv39\Scripts\Activate.ps1"
} else {
    Write-Host "Python 3.9 가상환경이 없습니다. 생성 중..." -ForegroundColor Yellow
    python -m venv venv39
    & "venv39\Scripts\Activate.ps1"
    pip install -r requirements.txt
}

# Node.js 서버 시작
Write-Host "`n[3/4] Node.js 서버 시작 (포트 8000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'src\backend\node'; npm start" -WindowStyle Normal

# Python TTS 서버 시작
Write-Host "`n[4/4] Python TTS 서버 시작 (포트 5000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'src\backend\Spark-TTS-main'; python webui.py" -WindowStyle Normal

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "모든 서버가 시작되었습니다!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "Node.js API 서버: http://localhost:8000" -ForegroundColor White
Write-Host "Python TTS 서버: http://localhost:5000" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
Write-Host "`n서버를 종료하려면 각 창을 닫으세요." -ForegroundColor Yellow
Read-Host "Press Enter to exit"
