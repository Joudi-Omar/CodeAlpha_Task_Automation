import os
import shutil

# Path to the Downloads folder
DOWNLOADS_FOLDER = os.path.expanduser('~/Downloads')

# File type categories and extensions
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []
}

def create_folders():
    """Create folders for each file category if they don't exist."""
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(DOWNLOADS_FOLDER, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    """Move files into their corresponding category folders."""
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        if os.path.isfile(file_path):  # To ensure that it's a file, not a folder
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    dest_path = os.path.join(DOWNLOADS_FOLDER, category, file_name)
                    shutil.move(file_path, dest_path)
                    moved = True
                    break

            # Move files that don't match any category to 'Others'
            if not moved:
                others_path = os.path.join(DOWNLOADS_FOLDER, 'Others', file_name)
                shutil.move(file_path, others_path)

def main():
    create_folders()
    move_files()
    print("Downloads folder organized successfully!")

if __name__ == "__main__":
    main()
