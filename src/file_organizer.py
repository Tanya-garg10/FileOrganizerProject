import os 
import shutil

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Others": []
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return

    for filename in os.listdir(directory):
        source = os.path.join(directory, filename)

        if os.path.isfile(source):
            category = get_category(filename)
            target_folder = os.path.join(directory, category)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            target = os.path.join(target_folder, filename)
            shutil.move(source, target)
            print(f"Moved {filename} → {category}/")

if __name__ == "__main__":
    target_dir = input("Enter the path to the directory to organize: ")
    organize_files(target_dir)