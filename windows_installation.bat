color 3
@echo off
cls

REM Winget ile FFmpeg kurulumu
echo FFmpeg kurulumu başlatılıyor...
winget install FFmpeg

REM Requirements.txt Kurulumu
echo Requirements.txt kurulumu başlatılıyor...
pip install -r -Requirements.txt

echo Kurulum tamamlandı.
pause
