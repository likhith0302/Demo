import json
import sys
import os

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PageObjects.login import LoginPage

test_data_path = 'C:\\Users\\likhi\\PycharmProjects\\PythonTesting\\Frameworks\\Data\\test_e2eFramework.json'

with open(test_data_path) as f:
    tset_data = json.load(f)
    test_list = tset_data['data']

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_items", test_list)
def test_e2e(browserInstance,test_list_items):
    driver = browserInstance
    driver.get(test_list_items["URL"])
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_items["username"],test_list_items["password"])
    print(shop_page.getTitle())
    shop_page.add_product_to_cart(test_list_items["productName"])
    cart_page = shop_page.go_to_cart()
    print(cart_page.getTitle())
    submit = cart_page.checkout()
    print(submit.getTitle())
    submit.Select_Country(test_list_items["country"])
    submit.Click_Check_Box()
    submit.Purchase()
    submit.Assert()

