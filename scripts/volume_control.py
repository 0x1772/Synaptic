import sys
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_volume():
    try:
        # Ses cihazlarını al
        devices = AudioUtilities.GetSpeakers()
        
        # İlk cihazın ses düzeyini al
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        # Ses düzeyini yüzde olarak dön
        return int(volume.GetMasterVolumeLevelScalar() * 100)
    
    except Exception as e:
        print("Ses düzeyi alınamadı:", str(e))
        return None

def set_volume(volume):
    try:
        # Ses düzeyini yüzde olarak ayarla
        volume = max(0, min(volume, 100))
        new_volume = volume / 100.0
        
        # Ses cihazlarını al
        devices = AudioUtilities.GetSpeakers()
        
        # İlk cihazın ses düzeyini ayarla
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        
        print("Ses düzeyi ayarlandı:", volume, "percent")
    
    except Exception as e:
        print("Ses düzeyi ayarlanamadı:", str(e))

# Komut satırı argümanlarına göre ses düzeyini kontrol et
if len(sys.argv) == 1 or sys.argv[1] == "g":
    volume = get_volume()
    if volume is not None:
        print("Mevcut ses düzeyi:", volume, "percent")

elif sys.argv[1] == "s" and len(sys.argv) >= 3:
    try:
        new_volume = int(sys.argv[2])
        set_volume(new_volume)
    except ValueError:
        print("Lütfen ayarlamak istediğiniz ses düzeyini belirtin")

else:
    print("Geçersiz komut veya argüman")
    print("Kullanım: python script.py [g] [s <ses_düzeyi>]")
    print("  g: Mevcut ses düzeyini gösterir")
    print("  s: Ses düzeyini belirli bir değere ayarlar")
