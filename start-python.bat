@echo off
echo ========================================
echo Python TTS 서버 시작
echo ========================================

echo Python 가상환경 활성화...
if exist "venv39\Scripts\activate.bat" (
    call venv39\Scripts\activate.bat
) else (
    echo Python 3.9 가상환경이 없습니다. 생성 중...
    python -m venv venv39
    call venv39\Scripts\activate.bat
    pip install -r requirements.txt
)

echo Python TTS 서버 시작 (포트 5000)...
cd src\backend\Spark-TTS-main
python webui.py

pause
