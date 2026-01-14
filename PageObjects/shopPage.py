from PageObjects.cartPage import CartItem
from selenium.webdriver.common.by import By
from Utils.browserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkOut = (By.CLASS_NAME, "btn-primary")

    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        items = self.driver.find_elements(*self.products)

        for item in items:
            if item.find_element(By.XPATH, "div/h4/a").text == product_name:
                item.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkOut).click()
        cart_page = CartItem(self.driver)
        return cart_page
