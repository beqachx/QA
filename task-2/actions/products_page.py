import random
from locators.products_page_locators import ProductsPageLocators
from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def select_random_product(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, ProductsPageLocators.PRODUCT_ITEMS)
        random_product = random.choice(products)
        random_product.click()

    def choose_size(self):
        sizes = self.driver.find_elements(By.CSS_SELECTOR, ProductsPageLocators.SIZES)
        random_size = random.choice(sizes)
        random_size.click()

    def choose_color(self):
        colors = self.driver.find_elements(By.CSS_SELECTOR, ProductsPageLocators.COLORS)
        random_color = random.choice(colors)
        random_color.click()