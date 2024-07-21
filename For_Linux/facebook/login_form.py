from selenium.webdriver.common.by import By


def login_form(driver):
    """Performs the login process using the provided driver."""
    while True:
        try:
            driver.implicitly_wait(10)
            email = ''
            password = ''
            login_div = driver.find_element(
                By.XPATH, '//*[@id="email"]'
            ).send_keys(email)
            pass_div = driver.find_element(
                By.XPATH, '//*[@id="pass"]'
            ).send_keys(password)
            login_button = driver.find_element(
                By.XPATH, '//*[@data-testid="royal_login_button"]'
            )
            login_button.click()
            driver.implicitly_wait(10)
            return driver
        except Exception as error:
            print(error)
            return 'ErrorLogin'
