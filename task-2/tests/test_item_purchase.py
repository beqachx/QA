import unittest
from selenium import webdriver
from actions.home_page import HomePage
from actions.products_page import ProductsPage
from actions.product_detail_page import ProductDetailPage
from time import sleep

URL = 'https://magento.softwaretestingboard.com/'

class TestItemPurchase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.home_page = HomePage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.product_detail_page = ProductDetailPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_item_purchase(self):
        # Click "Men" category
        self.home_page.click_men_category()

        # Scroll down to products (not implemented here)

        # Choose one item and click on it
        self.products_page.select_random_product()
        
        self.products_page.choose_size()
        self.products_page.choose_color()

        # On corresponding page of product detail
        # Click add to cart
        self.product_detail_page.add_to_cart()
        sleep(5)

        # Assert error messages if one exists
        cart_items_quantity = self.product_detail_page.get_items_quantity()
        self.assertTrue(1 == int(cart_items_quantity))

if __name__ == "__main__":
    unittest.main()
