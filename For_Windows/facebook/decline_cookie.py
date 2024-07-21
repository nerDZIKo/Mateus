from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


driver = webdriver.Chrome()
 
url = "https://www.facebook.com/"
    
def decline_cookie():
    driver.get(url) 
    search_text = "Odrzuć opcjonalne pliki cookie"
    wait = WebDriverWait(driver, 60)
    button = driver.find_elements(By.XPATH, "//*[@role='button']")
    if len(button) == 18:
        print('Przedstawiam Listę Elementów z Rola "button":')
        length = 0
        for element in button:
            length += 1
            print(str(length) + ' ' + element.text)
            if element.text == search_text:
                print('Klikam...')
                decline_button = element
                decline_button.click()
    return driver