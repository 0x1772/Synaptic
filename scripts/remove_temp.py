import os
import glob

def delete_temp_files():
    temp_folders = [
        os.path.join(os.environ["TEMP"]),
        os.path.join(os.environ["LOCALAPPDATA"], "Temp"),
        os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Temp")
    ]
    
    for folder in temp_folders:
        file_pattern = os.path.join(folder, "*")
        temp_files = glob.glob(file_pattern)
        
        for file in temp_files:
            try:
                if os.path.isfile(file):
                    os.remove(file)
                elif os.path.isdir(file):
                    os.rmdir(file)
            except Exception as e:
                print(f"Error deleting file/folder: {file}\n{str(e)}")

delete_temp_files()
