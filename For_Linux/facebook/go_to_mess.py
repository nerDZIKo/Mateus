import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.facebook.com/messages/t/"

def go_to_mess(driver, client):
    print('Przechodze...')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='navigation']")))
    print('Przechodze do grupy...')
    driver.get(url + client)
    print('Przechodze do klienta...')
    return driver
