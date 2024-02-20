from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class calculator_c():
    def __init__(self, browser, url):
        self._driver = browser
        self._driver.get(url)

    def find_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)

    def find_by_css(self, css):
        return self._driver.find_element(By.CSS_SELECTOR, css)

    def sum_15(self, delay):
        plus = self.find_by_xpath('//*[@id="calculator"]/div[2]/span[4]')
        equally = self.find_by_xpath('//*[@id="calculator"]/div[2]/span[15]')
        seven = self.find_by_xpath('//*[@id="calculator"]/div[2]/span[1]')
        eight = self.find_by_xpath('//*[@id="calculator"]/div[2]/span[2]')
        screen = self.find_by_xpath('//*[@id="calculator"]/div[1]/div')

        seven.click()
        plus.click()
        eight.click()
        equally.click()
        WebDriverWait(self._driver, delay).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))
        element = screen.get_attribute("textContent")
        return int(element)

    def waiter(self, wtr):
        input_l = self.find_by_css("#delay")
        input_l.clear()
        input_l.send_keys(wtr)