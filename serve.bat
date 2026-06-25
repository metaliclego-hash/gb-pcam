@echo off
cd /d "%~dp0"

echo ==========================================
echo  GBCam Web Server
echo ==========================================
echo.

:: Generate icons if missing
if not exist icon-180.png (
    echo Generating icons...
    python make_icons.py
    echo.
)

:: Show local IP for iPhone access instructions
echo Local URL:  http://localhost:8080
echo.
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    set IP=%%a
    setlocal enabledelayedexpansion
    set IP=!IP: =!
    echo LAN IP:     http://!IP!:8080
    endlocal
)
echo.
echo NOTE: iPhone requires HTTPS (except localhost).
echo For iPhone, use one of these options:
echo   A) Deploy to GitHub Pages (free, one-time setup)
echo   B) Run: ngrok http 8080  (get a temporary HTTPS URL)
echo.
echo Starting server...
echo Press Ctrl+C to stop.
echo.

python -m http.server 8080
pause
