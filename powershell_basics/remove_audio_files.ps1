$desktopPath = Join-Path -Path "C:\Users\$env:USERNAME\Masaüstü\Synaptic\audio_files"
New-Item -ItemType Directory -Path $desktopPath
$folderPath = Join-Path -Path $env:USERPROFILE -ChildPath "Path\To\Folder"
Remove-Item -Path $folderPath\* -Force -Recurse