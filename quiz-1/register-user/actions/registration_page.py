from selenium.webdriver.remote.webdriver import WebDriver
from locators.registration_locators import RegistrationLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_first_name(self, first_name: str) -> None:
        self.driver.find_element(By.XPATH, RegistrationLocators.NAME_INPUT).send_keys(first_name)

    def enter_email(self, email: str) -> None:
        self.driver.find_element(By.XPATH, RegistrationLocators.EMAIL_INPUT).send_keys(email)

    def click_register_button(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.SIGNUP_BTN).click()

    def enter_details(self, password: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('GENDER')).click()
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('PASSWORD')).send_keys(password)
        Select(self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('DAYS'))).select_by_index(1)
        Select(self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('MONTH'))).select_by_index(1)
        Select(self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('YEAR'))).select_by_index(16)
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('NEWSLETTER')).click()
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('OFFERS')).click()

        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('FIRST_NAME')).send_keys('gela')
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('LAST_NAME')).send_keys('mela')
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('COMPANY')).send_keys('BTU')
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('ADDRESS')).send_keys('rame, iseti, vitom, misasmarti')

        Select(self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('COUNTRY'))).select_by_index(2)
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('ADDRESS')).send_keys('asdasadsd')
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('STATE')).send_keys('asdasadsd')
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('CITY')).send_keys('asdasadsd')
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('ZIP')).send_keys(1121)
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('PHONE')).send_keys('555555555')

    def verify_created(self) -> None:
        page_text = self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.CREATED).text
        text_to_find = 'ACCOUNT CREATED!'
        assert text_to_find in page_text, f'{text_to_find} is not displayed'

    def verify_logged_in_as_username(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.CONTINUE).click()
        page_text = self.driver.find_element(By.XPATH, RegistrationLocators.LOGGED_IN_AS).text
        text_to_find = f'Logged in as '
        assert text_to_find in page_text, f'{text_to_find} is not displayed'

    def verify_delete_account(self) -> None:
        self.driver.find_element(By.XPATH, RegistrationLocators.DELETE_ACCOUNT).click()