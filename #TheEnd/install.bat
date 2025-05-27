@echo off
chcp 65001 >nul
title #ChoseNukPack Installer
color 0C
cls

echo.
echo ╔═══════════════════════════════════════════════════╗
echo ║          Installing Required Python Modules       ║
echo ║               By: #ChoseNukPack                   ║
echo ╚═══════════════════════════════════════════════════╝
echo.

:: Check if pip is available
where pip >nul 2>nul
if errorlevel 1 (
    echo [!] pip non trovato. Assicurati che Python sia installato correttamente.
    pause
    exit /b
)

echo [+] Inizio installazione librerie...
echo.

pip install discord.py
pip install colorama
pip install requests
pip install pystyle

echo.
echo [✔] Tutte le librerie sono state installate correttamente!
echo.
pause
exit
