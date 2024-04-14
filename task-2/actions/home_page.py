from locators.home_page_locators import HomePageLocators
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_men_category(self):
        self.driver.find_element(By.ID, HomePageLocators.MEN_CATEGORY_LINK).click()
