from selenium.webdriver.remote.webdriver import WebDriver
from locators.registration_locators import RegistrationLocators
from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_first_name(self, first_name: str) -> None:
        self.driver.find_element(By.ID, RegistrationLocators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.driver.find_element(By.ID, RegistrationLocators.LAST_NAME).send_keys(last_name)

    def enter_email(self, email: str) -> None:
        self.driver.find_element(By.ID, RegistrationLocators.EMAIL).send_keys(email)

    def enter_password(self, password: str) -> None:
        self.driver.find_element(By.ID, RegistrationLocators.PASSWORD).send_keys(password)

    def confirm_password(self, confirm_password: str) -> None:
        self.driver.find_element(By.ID, RegistrationLocators.CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_register_button(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.REGISTER_BUTTON).click()
