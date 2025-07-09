#from pathlib import Path
import os

def make_new_name(folder_name, file_name, extension):
    if (folder_name == "Slides") or (folder_name == "Lectures"):
        if file_name.startswith('ml') and file_name[2:].isdigit():
            lecture_number = int(file_name[2:])
            new_name = f"ML Lecture {lecture_number}{extension}"

        elif file_name.startswith('Lecture'): # previously renamed with a different policy
            lecture_number = int(file_name[8:])
            new_name = f"ML Lecture {lecture_number}{extension}"

        else :  # for lectures not named with a number
            new_name = f"ML {file_name}{extension}"

    if (folder_name.lower() == "assignments") or (folder_name.lower() == "exercise sheets"):
        if file_name.lower().startswith('assignment') and file_name[11:].isdigit():
            assignment_number = file_name[11:]
            new_name = f"ML Assignment {assignment_number}{extension}"

    return new_name


def rename_materials_in_folder(folder_name):  # actual renaming
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(parent_dir, folder_name)

    if not os.path.exists(folder_path):
        print ("Folder not found")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            name, extension = os.path.splitext(file_name)

            if (name.startswith('.')) or (extension != '.pdf'):  # skip system files and files other than pdf
                continue

            if not name.startswith('ML'):
                # print("trying to rename"+" "+file_name)
                new_name = make_new_name(folder_name, name, extension)
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                print(f"Renamed {file_name} to {new_name}")


def main ():
    rename_materials_in_folder("Slides")
    rename_materials_in_folder("Assignments")

if __name__ == "__main__":
    main()
