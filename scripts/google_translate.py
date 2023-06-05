import sys
from googletrans import Translator

def translate_text(text, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text

def main():
    if len(sys.argv) < 3:
        print("Hatalı kullanım. Örnek: python trans.py metin tr")
        return

    input_text = sys.argv[1]
    target_lang = sys.argv[2]

    translated_text = translate_text(input_text, target_lang)
    print(f"Çeviri: {translated_text}")

if __name__ == "__main__":
    main()
