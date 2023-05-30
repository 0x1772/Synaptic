import argparse
import ctypes
import time

def send_media_key(key):
    # Windows API kullanarak medya tuşlarını gönderme
    if key == 'play_pause':
        key_code = 0xB3
    elif key == 'stop':
        key_code = 0xB2
    elif key == 'ileri':
        key_code = 0xB0
    elif key == 'geri':
        key_code = 0xB1
    else:
        raise ValueError('Geçersiz medya tuşu: {}'.format(key))

    # Tuşu gönderme
    ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(key_code, 0, 0x2, 0)

def main():
    # Komut satırı argümanlarını ayrıştırma
    parser = argparse.ArgumentParser(description='Medya kontrolü için Python betiği')
    parser.add_argument('command', choices=['play_pause', 'stop', 'ileri', 'geri'],
                        help='Medya komutunu belirtin')
    args = parser.parse_args()

    # Medya komutunu gönderme
    send_media_key(args.command)

if __name__ == '__main__':
    main()
