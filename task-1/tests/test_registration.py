# tests/test_registration.py
import unittest
from selenium import webdriver
from actions.registration_page import RegistrationPage
from random import randint


URL = "https://magento.softwaretestingboard.com/customer/account/create/"
email = f"john.doe{randint(100, 100000)}@example.com"
password = f"assword{randint(1,1121)}$$$AA$#$%"

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.registration_page = RegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_successful_registration(self):
        # Fill in registration form with valid data
        self.registration_page.enter_first_name("John")
        self.registration_page.enter_last_name("Doe")
        self.registration_page.enter_email(email)
        self.registration_page.enter_password(password)
        self.registration_page.confirm_password(password)

        # Submit registration form
        self.registration_page.click_register_button()

        # Assert registration successful by checking URL
        self.assertIn("https://magento.softwaretestingboard.com/customer/account/", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
