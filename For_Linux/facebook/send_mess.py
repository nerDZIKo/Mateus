import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from scrapper_getter.prepare_memes import (
    get_images_from_meme_folder,
    read_sended_memes,
    copy_image_to_clipboard,
    JSONListDictManager_for_sended_memes,
    memes
)


def send_mess(driver, client_id):
    wait = WebDriverWait(driver, 10)
    print('Szukam...')
    time.sleep(5)
    try:
        messesage_area_list = driver.find_elements(
            By.XPATH, '//*[@aria-label="Wiadomość"]'
        )
        if len(messesage_area_list) == 0:
            print('Nie znaleziono pola wiadomości')
            return
        messesage_area = messesage_area_list[0]
    except NoSuchElementException:
        print('Nie znaleziono pola wiadomości')
        return

    get_images_from_meme_folder()
    testing_memes = memes

    manager = JSONListDictManager_for_sended_memes(
        'sended_memes' + client_id + '.json'
    )

    for meme in testing_memes:
        try:
            memes_to_check = read_sended_memes(client_id)
        except:
            print('BŁAD ODCZYTU MEME')

        if meme not in memes_to_check['name_of_files']:
            if 'mp4' not in meme:
                copy_image_to_clipboard('./memes/' + meme)
                manager.add(meme)
                messesage_area.send_keys(Keys.CONTROL, 'v')
                time.sleep(2)
                messesage_area.send_keys(Keys.ENTER)
        else:
            print('Juz wysłano te MEME')

    print('Memy wysłane...')



