from locators.product_detail_page_locators import ProductDetailPageLocators
from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, ProductDetailPageLocators.ADD_TO_CART_BUTTON).click()

    def get_items_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR,ProductDetailPageLocators.QUANTITY).text