import os
import random

def snap(): # Deletes half of the files in the current working directory, chosen randomly.
    folder_path = os.getcwd() # Current working directory
    print(f"Target Folder: {folder_path}")
    
     # Lists all files (ignore directories)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files: # if Empty
        print("No files found in the folder.")
        return
    
    #Fair and balanced, as all things should be... 
    print(f"Total files found: {len(files)}")
    print("Fair and balanced, as all things should be... ")
    
    files_to_delete = random.sample(files, len(files) // 2) #Floor division
    
    for file in files_to_delete:
        file_path = os.path.join(folder_path, file)
        try:
            os.remove(file_path)
            print(f"dusted: {file_path}")
        except Exception as e:
            print(f"Failed to dust {file_path}: {e}")
            
if __name__ == "__main__":
    snap()
