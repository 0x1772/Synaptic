def replace_language(file_path, new_language):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Değiştirilecek kısımların listesini oluştur
        replace_list = [('lang="tr"', 'lang="{}"'.format(new_language)),
                        ('language="tr"', 'language="{}"'.format(new_language))]
        
        # Kısımları değiştir
        for old_text, new_text in replace_list:
            content = content.replace(old_text, new_text)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print('Değiştirme işlemi başarıyla tamamlandı.')
    
    except FileNotFoundError:
        print('Dosya bulunamadı.')
    
    except Exception as e:
        print('Bir hata oluştu:', str(e))

if __name__ == '__main__':
    file_path = input('Dosya yolunu girin: ')
    new_language = input('Yeni dil değerini girin: ')
    replace_language(file_path, new_language)
