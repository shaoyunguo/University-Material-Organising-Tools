#from pathlib import Path
import os
import re

def make_new_name_lecture_numbers(folder_name, file_name, extension):
    numbers = re.search(r'\d+', file_name)
    if numbers:
        start = numbers.start()  # start position of the number
        number_str = file_name[start:]
        number = ''
        for char in number_str:
            if char.isdigit():
                number += char
            else:
                break

    new_name = f"{folder_name} {number}{extension}"

    return new_name

def rename_materials_in_folder(lecture_name, folder_name):
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(parent_dir, folder_name)

    if not os.path.exists(folder_path):
        print("Folder not found")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            name, extension = os.path.splitext(file_name)

            if (name.startswith('.')) or (extension != '.pdf'):  # skip system files and files other than pdf
                continue

            if not name.startswith('lecture_name'):
                # print("trying to rename"+" "+file_name)
                new_name = make_new_name_lecture_numbers(folder_name, name, extension)
                final_name = lecture_name + new_name
                new_path = os.path.join(folder_path, final_name)
                os.rename(file_path, new_path)
                print(f"Renamed {file_name} to {final_name}")

def main ():
    lecture_name = input("Enter the name of lecture: ")
    folder_name = input("Enter the name of the folder: ")
    # Option 1 : extract numbers, add name of lecture
    old_name = input("Enter one file name of the materials in the selected folder: ")
    rename_materials_in_folder(lecture_name, folder_name)


if __name__ == "__main__":
    main()
