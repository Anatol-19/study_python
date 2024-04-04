from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = ""

class DatatypesPage():
    def __init__(self, browser, url):
        self.driver = browser
        self.driver.get(url)
        
    # def finder(self, select):
    #     fnd = self.driver.find_element(By.CSS_SELECTOR, select)
    #     return fnd
    
    def finder(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, select))
        )
    
    # Поля формы
    ## First Name
    def field_First_name(self):
        field = self.finder("input[name='first-name']")
        return field
        
    def type_First_name(self, First_name):
        self.field_First_name().send_keys(First_name)
    
    def bkgr_First_name(self):
        return self.finder("#first-name").value_of_css_property("background-color")
    
    ## Last Name
    def field_Last_name(self):
        field = self.finder("input[name='last-name']")
        return field
    
    def type_Last_name(self, Last_name):
        self.field_Last_name().send_keys(Last_name)
        
    def bkgr_Last_name(self):
        return self.finder("#last-name").value_of_css_property("background-color")
     
    ## Address
    def field_Address(self):
        field = self.finder("input[name='address']")
        return field
    
    def type_Address(self, Address):
        self.field_Address().send_keys(Address)
    
    def bkgr_Address(self):
        return self.finder("#address").value_of_css_property("background-color")
    
    ## Zip code
    def field_Zip_code(self):
        field = self.finder("input[name='zip-code']")
        return field
    
    def type_Zip_code(self, Zip_code):
        self.field_Zip_code().send_keys(Zip_code)
    
    def bkgr_Zip_code(self):
        return self.finder("#zip-code").value_of_css_property("background-color")
    
    ## City
    def field_City(self):
        field = self.finder("input[name='city']")
        return field
       
    def type_City(self, City):
        self.field_City().send_keys(City)
    
    def bkgr_City(self):
        return self.field_City().value_of_css_property("background-color")
    
    ## Country
    def field_Country(self):
        field = self.finder("input[name='country']")
        return field
            
    def type_Country(self, Country):
        self.field_Country().send_keys(Country)
    
    def bkgr_Country(self):
        bkgr = self.field_Country().value_of_css_property("background-color")
        return bkgr
    
    ## Email
    def field_Email(self):
        field = self.finder("input[name='e-mail']")
        return field
    
    def type_Email(self, Email):
        self.field_Email().send_keys(Email)   

    def bkgr_Email(self):
        bkgr = self.field_Email().value_of_css_property("background-color")
        return bkgr
    
    ## Phone number
    def field_Phone_number(self):
        field = self.finder("input[name='phone']")
        return field
    
    def type_Phone_number(self, Phone_number):
        self.field_Phone_number().send_keys(Phone_number)
    
    def bkgr_Phone_number(self):
        bkgr = self.field_Phone_number().value_of_css_property("background-color")
        return bkgr
      
    ## Job position
    def field_Job_position(self):
        field = self.finder("input[name='job-position']")
        return field
      
    def type_Job_position(self, Job_position):
        self.field_Job_position().send_keys(Job_position)
    
    def bkgr_Job_position(self):
        bkgr = self.field_Job_position().value_of_css_property("background-color")
        return bkgr
    
    ## Company
    def field_Company(self):
        field = self.finder("input[name='company']")
        return field
        
    def type_Company(self, Company):
        self.field_Company().send_keys(Company)
        
    def bkgr_Company(self):
        bkgr = self.field_Company().value_of_css_property("background-color")
        return bkgr
    
    # кнопка
    def btn_Submit(self):
        bt = self.finder(".btn.btn-outline-primary.mt-3")
        return bt
        
    def clk_Submit(self):
        self.btn_Submit().click()
        