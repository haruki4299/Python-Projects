import os
import glob
import shutil

def create_folder(folder_name):
    folder_path = "./" + folder_name
    if os.path.exists(folder_path):
        print("Folder " + folder_name + " exists in desktop directory.")
    else:
        os.makedirs(folder_path)
        print("Created new folder " + folder_name + " in desktop directory.")

def move_file_to_folder(folder_name, file_name):
    
    cur_file_path = "./" + file_name
    new_file_path = "./" + folder_name + "/" + file_name
        
    shutil.move(cur_file_path, new_file_path)

def remove_screenshots():
    for file in glob.glob("Screenshot*.png"):
        print("Removing Screenshot: " + file)
        os.remove(file)
    
def main():
    # First Change working directory to Desktop
    path_to_desktop = os.path.expanduser("~/Desktop")

    os.chdir(path_to_desktop)
    
    print("Welcome to Desktop sorter")
    
    while True:
        mode = input("Enter 1 for Removing Screenshots. 2 for sorting files. Type 'quit' to quit: ")
        if mode == "1":
            remove_screenshots()
        elif mode == "2":
            substring_filename = input("enter a part of the file name that is common in all of the files you want to sort (ex. '.png' '.txt' 'HW'): ")
            file_name = "*" + substring_filename + "*"
            folder_name = input("Enter the name of the folder you want to put these files in: ")
            create_folder(folder_name)
            
            for file in glob.glob(file_name):
                move_file_to_folder(folder_name, file)
            
        elif mode in ["quit", "q"]:
            break 
        else:
            print("Not a valid mode. Reselect")
            
        
    
if __name__ == '__main__':
    main()