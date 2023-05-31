import subprocess

def run_powershell_script(script_path):
    try:
        subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")

# PowerShell betiğinin tam dosya yolunu belirtin
powershell_script_path = 'C:\\Users\\realh\\Masaüstü\\Synaptic\\powershell_basics\\lock_windows.ps1'

run_powershell_script(powershell_script_path)
