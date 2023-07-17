import os
import shutil

def organize_photos(folder_name):
    # Ana klasördeki dosyaların listesi
    files = os.listdir(folder_name)
    
    # Klasör oluşturma ve numaralandırma işlemi
    folder_count = 1
    current_folder = f"{folder_name}_1"
    os.makedirs(current_folder, exist_ok=True)
    
    for file in files:
        source_path = os.path.join(folder_name, file)
        dest_path = os.path.join(current_folder, file)
        shutil.move(source_path, dest_path)
        
        # Her klasörde 1800 dosya olacak şekilde klasörleri ayırma
        if len(os.listdir(current_folder)) == 1800:
            folder_count += 1
            current_folder = f"{folder_name}_{folder_count}"
            os.makedirs(current_folder, exist_ok=True)

if __name__ == "__main__":
    folder_name = "Photos from 2020"
    organize_photos(folder_name)
