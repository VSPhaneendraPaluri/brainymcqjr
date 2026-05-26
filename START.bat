@echo off
REM MCQ Quiz Master - Quick Start Script

echo.
echo ╔═══════════════════════════════════════════════════╗
echo ║  BrainyMCQ Junior - Quick Start                   ║
echo ╚═══════════════════════════════════════════════════╝
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
    echo.
)

REM Activate virtual environment
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

REM Check if dependencies installed
echo [3/4] Installing dependencies...
pip install -q -r requirements.txt
echo ✓ Dependencies installed
echo.

REM Start the server
echo [4/4] Starting MCQ Quiz Master...
echo.
python run.py

pause
