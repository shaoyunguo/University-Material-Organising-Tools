from pathlib import Path
import os

def rename_materials_in_folder(folder_name):
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(parent_dir, folder_name)

    if not os.path.exists(folder_path):
        print ("Folder not found")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            name, extension = os.path.splitext(file_name)

            if name.startswith('.'):  # skip system files
                continue

            if (folder_name == "Slides" )| (folder_name == "Lectures") :
                if name.startswith('ml') and name[2:].isdigit():
                    lecture_number = int(name[2:])
                    new_name = f"ML Lecture {lecture_number}{extension}"
                    new_path = os.path.join(folder_path, new_name)
                    os.rename(file_path, new_path)
                    print(f"Renamed {file_name} to {new_name}")

            if (folder_name.lower() == "assignments") | (folder_name == "exercise Sheets") :
                if name.lower().startswith('assignment') and name[11:].isdigit():
                    assignment_number = name[11:]
                    new_name = f"ML Assignment {assignment_number}{extension}"
                    new_path = os.path.join(folder_path, new_name)
                    os.rename(file_path, new_path)
                    print(f"Renamed {file_name} to {new_name}")



def main ():
    rename_materials_in_folder("Slides")
    rename_materials_in_folder("Assignments")

if __name__ == "__main__":
    main()
