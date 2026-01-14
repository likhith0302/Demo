from selenium.webdriver.common.by import By
from PageObjects.submitPage import SubmitItems
from Utils.browserUtils import BrowserUtils

class CartItem(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkOut = (By.CLASS_NAME, "btn-success")

    def checkout(self):
        self.driver.find_element(*self.checkOut).click()
        submit_page = SubmitItems(self.driver)
        return submit_page