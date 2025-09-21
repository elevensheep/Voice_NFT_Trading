@echo off
echo ========================================
echo Flask TTS Server Starting
echo ========================================

echo Activating Python virtual environment...
if exist "venv39\Scripts\activate.bat" (
    call venv39\Scripts\activate.bat
) else (
    echo Python 3.9 virtual environment not found. Creating...
    python -m venv venv39
    call venv39\Scripts\activate.bat
    pip install -r requirements.txt
)

echo Starting Flask TTS server (Port 5000)...
cd src\backend\Spark-TTS-main
python webui.py

pause

