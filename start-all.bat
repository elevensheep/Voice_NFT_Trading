@echo off
echo ========================================
echo Voice NFT Trading Platform Starting
echo ========================================

echo.
echo [1/4] Switching to Node.js 16...
call nvm use 16.20.2
if %errorlevel% neq 0 (
    echo Failed to switch to Node.js 16
    pause
    exit /b 1
)

echo.
echo [2/4] Activating Python virtual environment...
if exist "venv39\Scripts\activate.bat" (
    call venv39\Scripts\activate.bat
) else (
    echo Python 3.9 virtual environment not found. Creating...
    python -m venv venv39
    call venv39\Scripts\activate.bat
    pip install -r requirements.txt
)

echo.
echo [3/4] Starting Node.js server (Port 8000)...
start "Node.js Server" cmd /k "cd src\backend\node && npm start"

echo.
echo [4/4] Starting Python TTS server (Port 5000)...
start "Python TTS Server" cmd /k "cd src\backend\Spark-TTS-main && python webui.py"

echo.
echo ========================================
echo All servers have been started!
echo ========================================
echo Node.js API Server: http://localhost:8000
echo Python TTS Server: http://localhost:5000
echo ========================================
echo.
echo Close each window to stop the servers.
pause
