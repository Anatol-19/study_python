from selenium.webdriver.common.by import By

class ShopMethods():
    def __init__(self, browser, url):
        self._driver = browser
        self._driver.get(url)

    def find(self, select):
        finder = self._driver.find_element(By.CSS_SELECTOR, select)
        return finder
    
    def authorization(self, login, password):
        login_field = self.find("#user-name")
        password_field = self.find("#password")

        login_field.clear()
        login_field.send_keys(login)
        password_field.clear()
        password_field.send_keys(password)

        self.find("#login-button").click()

    def add_to(self):
        self.find("#add-to-cart-sauce-labs-backpack").click()
        self.find("#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.find("#add-to-cart-sauce-labs-onesie").click()
    
    def go_to(self):
        self.find(".shopping_cart_link").click()

    def clk_check(self):
        self.find("#checkout").click()

    def input_form(self, f_name, l_name, zip_code):
        self.find("#first-name").send_keys(f_name)
        self.find("#last-name").send_keys(l_name)
        self.find("#postal-code").send_keys(zip_code)

    def clk_cnt(self):
        self.find("#continue").click()

    def rd_total(self):
        return self.find(".summary_info_label.summary_total_label").text