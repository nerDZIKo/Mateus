import os

def get_images_from_meme_folder():
    try:
        path = 'memes'
        if not os.path.exists(path):
            print(f"Directory '{path}' does not exist.")
            return []

        if not os.path.isdir(path):
            print(f"'{path}' is not a directory.")
            return []

        list_of_files = os.listdir(path)
        return list_of_files
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Check the current working directory
print(f"Current working directory: {os.getcwd()}")

# Get list of files
files = get_images_from_meme_folder()
print(files)
