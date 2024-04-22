from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = ""

class Shop_MainPage():
    def __init__(self, browser, url):
        self.driver = browser
        self.driver.get(url)
    
    def finder_CSS(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, select))
        )
        
    # def finder_Name(self, select, timeout=10):
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.visibility_of_element_located((By.NAME, select))
    #     )
    
    def finder_Xpath(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, select))
        )
    
    # Авторизация
    #  Добавьте в корзину товары:
    ## Sauce Labs Backpack
    ## Sauce Labs Bolt T-Shirt
    ## Sauce Labs Onesie
    # Перейдите в корзину.