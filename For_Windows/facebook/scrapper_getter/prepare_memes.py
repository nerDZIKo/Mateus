from PIL import Image
import io
import win32clipboard
import os
import json

def get_images_from_meme_folder():
    path = 'memes'
    list_of_files = os.listdir(path)
    return list_of_files

memes = get_images_from_meme_folder()

def copy_image_to_clipboard(image_path):
    image = Image.open(image_path)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def save_sent_meme(meme_name):
    with open('sent_memes.json', 'w') as file:
        json.dump(meme_name, file)

def read_sended_memes(client):
    try:
        with open('sended_memes' + client + '.json', 'r') as file:
            sended_memes_json = json.load(file)
            return sended_memes_json
    except FileNotFoundError:
        sended_memes_json = None
        return None
    except json.JSONDecodeError:
        print('The file "sended_memes.json" is not a valid json file')
        return None

class JSONListDictManager_for_sended_memes:
    def __init__(self, file_name):
        self.file_name = file_name
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump({"name_of_files": []}, file, indent=4)

    def read(self):
        with open(self.file_name, 'r') as file:
            return json.load(file)

    def add(self, new_data):
        with open(self.file_name, 'r+') as file:
            data = json.load(file)
            if new_data not in data['name_of_files']:
                data['name_of_files'].append(new_data)
                file.seek(0)
                json.dump(data, file, indent=4)

    def remove_all(self):
        with open(self.file_name, 'w') as file:
            json.dump({"name_of_files": []}, file, indent=4)

