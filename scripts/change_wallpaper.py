import os
import random
import ctypes

def set_wallpaper(file_path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)

def get_random_image(file_path):
    image_extensions = ['.png', '.jpg', '.jpeg']  # Desteklenen resim uzantıları

    image_files = [file for file in os.listdir(file_path) if os.path.splitext(file)[1].lower() in image_extensions]
    
    if len(image_files) > 0:
        random_image = random.choice(image_files)
        return os.path.join(file_path, random_image)
    else:
        return None

def main():
    desktop_path = os.path.expanduser('~/Masaüstü/Synaptic/wallpaper_path')  # Kullanıcının masaüstü yolu

    image_path = get_random_image(desktop_path)
    
    if image_path:
        set_wallpaper(image_path)
        print("Masaüstü arkaplanı başarıyla değiştirildi!")
    else:
        print("Belirtilen dizinde resim bulunamadı.")

if __name__ == '__main__':
    main()
