import pytest
from PageObject_7_1 import DatatypesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    # Закройте браузер.
    driver.quit()
    
@pytest.mark.parametrize("First_name, Last_name, Address, Email, Phone_number, Zip_code, City, Country, Job_position, Company", [
    ("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
])

def test_1(browser, First_name, Last_name, Address, Email, Phone_number, Zip_code, City, Country, Job_position, Company):
# 1. Откройте сайт магазина
    page = DatatypesPage(browser, "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# 2. Заполните форму значениями
    page.type_First_name(First_name)
    page.type_Last_name(Last_name)
    page.type_Address(Address)
    page.type_Zip_code(Zip_code)
    page.type_City(City)
    page.type_Country(Country)
    page.type_Email(Email)
    page.type_Phone_number(Phone_number)
    page.type_Job_position(Job_position)
    page.type_Company(Company)
    
# 3. Нажмите кнопку Submit.
    page.clk_Submit()
# Дождаться исчезновения модального окна
    # WebDriverWait(browser, 10).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))

    
# 4. Проверьте (assert), что поле `Zip code` подсвечено красным. rgba(248, 215, 218, 1)
    assert page.bkgr_Zip_code() == "rgba(248, 215, 218, 1)"
    
# 5. Проверьте (assert), что остальные поля подсвечены зеленым. rgba(209, 231, 221, 1)
    assert page.bkgr_First_name() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Last_name() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Address() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_City() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Country() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Email() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Phone_number() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Job_position() == 'rgba(209, 231, 221, 1)'
    assert page.bkgr_Company() == 'rgba(209, 231, 221, 1)'