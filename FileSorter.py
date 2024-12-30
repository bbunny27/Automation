import os, shutil
from pathlib import Path

def Sort():
    downloads_path = r"C:\Users\tytyd\Downloads"

    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv', '.pptx', '.epub'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'Video': ['.mp4', '.mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Code': ['.py', '.js', '.html', '.css', '.json', '.xml'],
        'Installers': ['.exe', '.msi', '.iso', '.ova', '.jar']

        }

    try:
        for filename in os.listdir(downloads_path):
                    file_path = os.path.join(downloads_path, filename)
                    
                    
                    # Get file extension
                    file_ext = os.path.splitext(filename)[1].lower()
                    
                    # Find matching category
                    for category, ext_list in extensions.items():
                        if file_ext in ext_list:
                            dest_path = os.path.join(downloads_path, category, filename)
                            
                            shutil.move(file_path, dest_path)
                            break
                    
    except Exception as e:
        print(f"Error: {str(e)}")

Sort()