from selenium.webdriver.common.by import By

def test_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    driver.find_element(By.XPATH, "//th[@role='columnheader'][1]").click()
    list1 = []
    ele = driver.find_elements(By.XPATH, "//tr/td[1]")

    for i in ele:
        list1.append(i.text)

    list2 = list1.copy()
    list1.sort()
    assert list1 == list2