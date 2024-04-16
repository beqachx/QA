from selenium.webdriver.remote.webdriver import WebDriver
from locators.login_locators import LogInLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_password(self, password: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, LogInLocators.PASSWORD_INPUT).send_keys(password)

    def enter_email(self, email: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, LogInLocators.EMAIL_INPUT).send_keys(email)

    def click_login_button(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, LogInLocators.LOGIN_BTN).click()


    def verify_logged_in_as_username(self) -> None:
        page_text = self.driver.find_element(By.XPATH, LogInLocators.LOGGED_IN_AS).text
        text_to_find = f'Logged in as '
        assert text_to_find in page_text, f'{text_to_find} is not displayed'
    
    def verify_delete_account(self) -> None:
        self.driver.find_element(By.XPATH, LogInLocators.DELETE_ACCOUNT).click()