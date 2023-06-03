import os
from git import Repo
import shutil

def clone_repo(repo_url, destination_folder):
    Repo.clone_from(repo_url, destination_folder)

def replace_files(source_folder, destination_folder):
    for file_name in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.copyfile(source_file, destination_file)

# GitHub deposunun URL'si
repo_url = 'https://github.com/0x1772/Synaptic/'
# İndirilen dosyaların yerleştirileceği hedef klasör kendinize göre değiştirmelisiniz
destination_folder = '/path/to/destination/folder'

# Depoyu klonlama
clone_repo(repo_url, destination_folder)

# Değiştirilecek yeni dosyaların yer aldığı klasör kendinize göre değiştirmelisiniz
source_folder = '/path/to/source/folder'

# Mevcut dosyaların yer aldığı hedef klasördeki dosyaları silme
for file_name in os.listdir(destination_folder):
    file_path = os.path.join(destination_folder, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Yeni dosyaları hedef klasöre kopyalama
replace_files(source_folder, destination_folder)

print("Dosyalar başarıyla güncellendi")