import sys
import requests

def para_birimi_fiyati(sembol):
    url = f"https://api.exchangerate-api.com/v4/latest/TRY"
    response = requests.get(url)
    data = response.json()

    if "rates" in data:
        return data["rates"].get(sembol)
    else:
        return None

if len(sys.argv) < 2:
    print("Lütfen bir para birimi sembolü girin.")
    sys.exit(1)

sembol = sys.argv[1]
fiyat = para_birimi_fiyati(sembol)

if fiyat:
    tl_fiyat = 1 / fiyat  # Girilen para biriminin TL karşılığı
    print(f"1 {sembol} = {tl_fiyat:.2f} TL")
else:
    print("Geçerli bir para birimi sembolü girmediniz veya fiyat bulunamadı.")
