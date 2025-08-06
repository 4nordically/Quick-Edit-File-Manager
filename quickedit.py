import os
import shutil
from datetime import datetime

def clear_folder(folder_path):
    """Clears all files in the specified folder"""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {filename}")
        except Exception as e:
            print(f"Error deleting file: {filename} - {e}")

def rename_files_bulk(folder_path):
    """Renames all files in the specified folder with a bulk rename"""
    print("How should the files be named?")
    print("A | (Number) {Name}")
    print("B | {Number}")
    print("C | {Date Created}")
    choice = input("Enter option: ")

    if choice.upper() == "A":
        name = input("Enter name: ")
        files = sorted(os.listdir(folder_path), key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        for index, filename in enumerate(files):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1]
                new_filename = f"{index+1} {name}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} to {new_filename}")
    elif choice.upper() == "B":
        files = sorted(os.listdir(folder_path), key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        for index, filename in enumerate(files):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1]
                new_filename = f"{index+1}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} to {new_filename}")
    elif choice.upper() == "C":
        files = sorted(os.listdir(folder_path), key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
        for filename in files:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                timestamp = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H-%M-%S")
                file_extension = os.path.splitext(filename)[1]
                new_filename = f"{timestamp}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed file: {filename} to {new_filename}")
    else:
        print("Invalid choice. Please try again.")

def main():
    print("Hello, which folder would you like to organise?")
    folder_name = input("Enter folder name: ")
    folder_path = os.path.join(os.getcwd(), folder_name)

    if not os.path.exists(folder_path):
        print("Folder does not exist. Please create the folder and try again.")
        return

    print("What action should happen?")
    print("A | Clear Folder")
    print("B | Rename Files (Bulk)")
    print("C | Cancel")
    choice = input("Enter choice: ")

    if choice.upper() == "A":
        confirm = input(f"Are you sure you want to clear the folder '{folder_name}'? (y/n): ")
        if confirm.lower() == "y":
            clear_folder(folder_path)
        else:
            print("Action cancelled.")
    elif choice.upper() == "B":
        rename_files_bulk(folder_path)
    elif choice.upper() == "C":
        print("Action cancelled.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
