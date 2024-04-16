# tests/test_registration.py
from time import sleep
import unittest
from selenium import webdriver
from actions.login_page import LoginPage
from random import randint
from selenium.webdriver.common.by import By
from locators.login_locators import LogInLocators

URL = "https://automationexercise.com/"
email = "rasada@example.com"
password = "asdasd"

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        expected_title = "Automation Exercise"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

        self.registration_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def goto_login(self):
        self.driver.find_element(By.XPATH, LogInLocators.LOGIN_SIGNUP_BTN).click()

    def test_successful_login(self):
        self.goto_login()
        self.registration_page.enter_email(email)
        self.registration_page.enter_password(password)
        self.registration_page.click_login_button()
        self.registration_page.verify_not_logged_in()

if __name__ == "__main__":
    unittest.main()
