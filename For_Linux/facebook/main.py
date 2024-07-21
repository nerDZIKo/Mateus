import os
import sys
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException

from decline_cookie import decline_cookie
from login_form import login_form
from go_to_mess import go_to_mess
from send_mess import send_mess

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
MODULE_DIR = os.path.join(PARENT_DIR, 'jebzdzidy_scrapper')
if MODULE_DIR not in sys.path:
    sys.path.append(MODULE_DIR)

from second_mateus import scrape_memes

CLIENT_IDS = []

SLEEP_TIME = 7200
not_logged = False


def main(not_logged):
    while True:
        scrape_memes()
        if not_logged == False:
            try:
                driver = decline_cookie()
                decline_cookie_driver = driver
                login_form_driver = login_form(decline_cookie_driver)

                while login_form_driver == 'ErrorLogin':
                    print('ErrorLogin')
                    driver = decline_cookie()
                    decline_cookie_driver = driver
                    login_form_driver = login_form(decline_cookie_driver)
                    print('LoginForm')
            except StaleElementReferenceException:
                continue
            except Exception as error:
                print(error)
                
        not_logged = True

        for client in CLIENT_IDS:
            print(client)
            go_to_mess_driver = go_to_mess(login_form_driver, client)
            send_mess_driver = send_mess(go_to_mess_driver, client)
        print('Zadanie Wykonane')
        sleep(SLEEP_TIME)


if __name__ == '__main__':
    main(not_logged)


