# tests/test_registration.py
import unittest
from selenium import webdriver
from actions.registration_page import RegistrationPage
from random import randint
from selenium.webdriver.common.by import By
from locators.registration_locators import RegistrationLocators

URL = "https://automationexercise.com/"
first_name = "John"
email = f"john.doe{randint(100, 100000)}@example.com"
password = f"password{randint(1,1121)}$$$AA$#$%"

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        expected_title = "Automation Exercise"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

        self.registration_page = RegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def goto_register(self):
        self.driver.find_element(By.XPATH, RegistrationLocators.LOGIN_SIGNUP_BTN).click()

    def test_signup_availability(self):
        self.goto_register()
        new_user_signup_text = self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.SIGNUP_FORM).text
        print(new_user_signup_text)
        assert 'New User Signup' in new_user_signup_text, "'New User Signup!' text is not displayed"

    def test_successful_registration(self):
        self.goto_register()
        self.registration_page.enter_first_name(first_name)
        self.registration_page.enter_email(email)

        self.registration_page.click_register_button()

        page_text = self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.ENTER_ACCOUNT_INFO_SELECTOR).text
        text_to_find = 'ENTER ACCOUNT INFORMATION'
        assert text_to_find in page_text, f'{text_to_find} is not displayed'

        self.registration_page.enter_details(password)
        self.driver.find_element(By.CSS_SELECTOR, RegistrationLocators.DETAILS_SELECTORS.get('SUBMIT_BTN')).click()

        self.registration_page.verify_created()
        self.registration_page.verify_logged_in_as_username()
        # self.registration_page.verify_delete_account()

if __name__ == "__main__":
    unittest.main()
