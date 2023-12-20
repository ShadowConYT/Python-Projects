import os 
import shutil

def create_folder(path: str, extension: str):

    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def sort_files(source_path: str):
    
    for rootdir, subdir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(rootdir, filename) # rootDir/filname/file.ext
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)
                shutil.move(file_path, target_path)

def remove_empty_folders(source_path: str):

    for rootdir, subdir, filename in os.walk(source_path, topdown=False):
        for current_dir in subdir:
            folder_path: str = os.path.join(rootdir, current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():
    user_input: str = input("Enter the path of your file/folder to sort: ")

    if os.path.exists(user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)

        print(f'Files have been sorted Successfully! \n There were totally {len(next(os.walk(user_input))[1])} file structures \n {[dir for i, dir in enumerate(os.listdir(user_input))]}')
    else:
        print("The specified path does not exist.")

if __name__ == "__main__":
    main()