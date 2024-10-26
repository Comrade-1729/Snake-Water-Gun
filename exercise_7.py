'''
    Clear the Clutter
'''
import os

def rename_files_in_folder(folder_path):
    ''' 
        A list of all files in the given folder 
    '''
    files = os.listdir(folder_path)

    # Filter for PNG files or any other files (for all files, skip the filtering)
    png_files = [file for file in files if file.lower().endswith('.png')]

    # Rename PNG files sequentially
    for index, file_name in enumerate(png_files, start=1):
        old_path = os.path.join(folder_path, file_name)   # to get full path of file
        new_name = f"{index}.png"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{file_name}' to '{new_name}'")

    # To rename all files, uncomment the following block:
    # for index, file_name in enumerate(files, start=1):
    #     old_path = os.path.join(folder_path, file_name)
    #     extension = os.path.splitext(file_name)[1]  # Get file extension
    #     new_name = f"{index}{extension}"
    #     new_path = os.path.join(folder_path, new_name)
    #     os.rename(old_path, new_path)
    #     print(f"Renamed '{file_name}' to '{new_name}'")

# Replace with the path of your folder
FOLDER_PATH = r'D:\CODE\Exercises\cluttered_folder'
rename_files_in_folder(FOLDER_PATH)
