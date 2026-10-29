@echo off
setlocal
title Claude Code (free) launcher

REM ===== Settings =====
set PORT=8082
set PROXY_URL=http://localhost:%PORT%
set PROXY_TOKEN=freecc
set REPO=git+https://github.com/Alishahryar1/free-claude-code.git

REM Work from the folder this script lives in
cd /d "%~dp0"

REM ===== 1. Clear stale proxy processes on the port =====
echo Checking port %PORT% for old proxy processes...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort %PORT% -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }"

REM ===== 2. Clear model overrides that would beat the .env file =====
set MODEL=
set MODEL_OPUS=
set MODEL_SONNET=
set MODEL_HAIKU=

REM ===== 3. Find a way to start the proxy server (fcc-server) =====
set "PROXY_CMD="
where fcc-server >nul 2>nul
if not errorlevel 1 set "PROXY_CMD=fcc-server"

if not defined PROXY_CMD if exist "%USERPROFILE%\.local\bin\fcc-server.exe" set "PROXY_CMD=%USERPROFILE%\.local\bin\fcc-server.exe"

if not defined PROXY_CMD (
  where uv >nul 2>nul
  if not errorlevel 1 set "PROXY_CMD=uv tool run --from %REPO% fcc-server"
)

if not defined PROXY_CMD (
  echo ERROR: neither fcc-server nor uv was found.
  echo Install uv first, then run:
  echo   uv tool install --force %REPO%
  pause
  exit /b 1
)

echo Starting proxy with: %PROXY_CMD%
start "free-claude-code proxy" cmd /k %PROXY_CMD%

REM ===== 4. Wait until the proxy answers (max ~90 seconds) =====
set /a tries=0
:wait
curl.exe -s -o NUL %PROXY_URL%/v1/models
if not errorlevel 1 goto ready
set /a tries+=1
if %tries% GEQ 90 (
  echo ERROR: proxy did not start. Check the proxy window for errors.
  pause
  exit /b 1
)
timeout /t 1 /nobreak >nul
goto wait

:ready
echo Proxy is up at %PROXY_URL%

REM ===== 5. Launch Claude Code pointed at the proxy =====
set ANTHROPIC_BASE_URL=%PROXY_URL%
set ANTHROPIC_AUTH_TOKEN=%PROXY_TOKEN%
start "Claude Code" cmd /k claude

endlocal