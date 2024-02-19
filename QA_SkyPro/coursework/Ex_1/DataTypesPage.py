from selenium.webdriver.common.by import By


class DataTypes:
    def __init__(self, driver):
        self._driver = driver

    def open_page(self ,url):
        self._driver.get(url)

    def input_form(self, inpt):
        for i in inpt:
            element = self._driver.find_element(By.NAME, i)
            element.clear()
            element.send_keys(inpt[i])

    def submit_clk(self):
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()