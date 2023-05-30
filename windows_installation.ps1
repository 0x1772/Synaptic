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
Pause
