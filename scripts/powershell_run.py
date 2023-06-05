import sys
import subprocess

def run_powershell_script(script_path):
    try:
        subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")

if len(sys.argv) < 2:
    print("Lütfen PowerShell betiğinin dosya yolunu argüman olarak belirtin.")
else:
    powershell_script_path = sys.argv[1]
    run_powershell_script(powershell_script_path)
