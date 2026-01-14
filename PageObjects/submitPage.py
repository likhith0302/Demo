from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utils.browserUtils import BrowserUtils


class SubmitItems(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.country = (By.ID, "country")
        self.India = (By.XPATH, "//a[text()='India']")
        self.check = (By.CLASS_NAME, "checkbox-primary")
        self.purchase = (By.CLASS_NAME, "btn-success")
        self.alert = (By.CLASS_NAME, "alert-success")


    def Select_Country(self,key):
        self.driver.find_element(*self.country).send_keys(key)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.India))
        self.driver.find_element(*self.India).click()

    def Click_Check_Box(self):
        self.driver.find_element(*self.check).click()

    def Purchase(self):
        self.driver.find_element(*self.purchase).click()

    def Assert(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.alert))
        text = self.driver.find_element(*self.alert).text
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in text