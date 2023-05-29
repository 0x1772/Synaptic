import sys
import codecs
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
        print("Ses duzeyi alinamadi:", str(e))
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
        
        print("Ses duzeyi ayarlandi")
    
    except Exception as e:
        print("Ses duzeyi ayarlanamadi:", str(e))

# Komut satırı argümanlarına göre ses düzeyini kontrol et
if len(sys.argv) == 1 or sys.argv[1] == "g":
    volume = get_volume()
    if volume is not None:
        print("Mevcut ses duzeyi: {} percent".format(volume))

elif sys.argv[1] == "s" and len(sys.argv) >= 3:
    try:
        new_volume = int(sys.argv[2])
        set_volume(new_volume)
    except ValueError:
        print("Ayarlamak istediginiz ses duzeyini belirtin")

else:
    print("Gecersiz komut veya arguman")
    print("Kullanim: python script.py [g] [s <ses_duzeyi>]")
    print("  g: Mevcut ses duzeyini gosterir")
    print("  s: Ses duzeyini belirli bir degere ayarlar")
