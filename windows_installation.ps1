# FFmpeg kurulumu
Write-Host "FFmpeg kurulumu başlatılıyor..."
winget install FFmpeg

# Requirements.txt Kurulumu
Write-Host "Requirements.txt kurulumu başlatılıyor..."
pip install -r -Requirements.txt

$file = "$env:userprofile\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\aiml\Kernel.py"
$output = "$file.tmp"

(Get-Content -Path $file) | ForEach-Object {
    $_ -replace "time\.clock", "time.perf_counter"
} | Set-Content -Path $output

Move-Item -Path $output -Destination $file -Force

Write-Host "Dosya güncellendi: $file"

$directory = Join-Path -Path $PSScriptRoot -ChildPath "log_directory"
New-Item -ItemType Directory -Path $directory -Force | Out-Null
# Kullanıcıdan log dizinini al
$logDirectory = Read-Host -Prompt "Log dizinini girin (örn: C:\logs):"

# main.py dosyasının yolunu al
$scriptPath = Split-Path -Parent -Path $MyInvocation.MyCommand.Path

# main.py dosyasını oku
$content = Get-Content -Path "$scriptPath\main.py"

# Yeni log dizinini kullanarak main.py dosyasını güncelle
$content = $content -replace 'log_directory = ".+"', "log_directory = '$logDirectory'"

# Güncellenmiş içeriği main.py dosyasına yaz
Set-Content -Path "$scriptPath\main.py" -Value $content

Write-Host "main.py dosyası güncellendi."
