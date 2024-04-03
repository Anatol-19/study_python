import click
from selenium.webdriver.common.by import By

url = ""

class DatatypesPage():
    def __init__(self, browser, url):
        self.driver = browser
        self.driver.get(url)
        
    def finder(self, select):
        fnd = self.driver.find_element(By.CSS_SELECTOR, select)
        return fnd
    
    def type_First_name(self, First_name):
        self.finder("input[name='first-name']").send_keys(First_name)
        
    def type_Last_name(self, Last_name):
        self.finder("input[name='last-name']").send_keys(Last_name)
        
    def type_Address(self, Address):
        self.finder("input[name='address']").send_keys(Address)
        
    def type_Zip_code(self, Zip_code):
        self.finder("input[name='zip-code']").send_keys(Zip_code)
        
    def type_City(self, City):
        self.finder("input[name='city']").send_keys(City)
            
    def type_Country(self, Country):
        self.finder("input[name='country']").send_keys(Country)
    
    def type_Email(self, Email):
        self.finder("input[name='e-mail']").send_keys(Email)   
        
    def type_Phone_number(self, Phone_number):
        self.finder("input[name='phone']").send_keys(Phone_number)
        
    def type_Job_position(self, Job_position):
        self.finder("input[name='job-position']").send_keys(Job_position)
        
    def type_Company(self, Company):
        self.finder("input[name='company']").send_keys(Company)
        
    def clk_Submit(self):
        self.finder(".btn.btn-outline-primary.mt-3").click()
        