import pytest
from PageObject_7_1 import DatatypesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    # Закройте браузер.
    driver.quit()
    
@pytest.mark.parametrize("field_name, field_value, expected_color", [
    ("First_name", "Иван", "rgba(209, 231, 221, 1)"),
    ("Last_name", "Петров", "rgba(209, 231, 221, 1)"),
    ("Address", "Ленина, 55-3", "rgba(209, 231, 221, 1)"),
    ("City", "Москва", "rgba(209, 231, 221, 1)"),
    ("Country", "Россия", "rgba(209, 231, 221, 1)"),
    ("Email", "test@skypro.com", "rgba(209, 231, 221, 1)"),
    ("Phone_number", "+7985899998787", "rgba(209, 231, 221, 1)"),
    ("Job_position", "QA", "rgba(209, 231, 221, 1)"),
    ("Company", "SkyPro", "rgba(209, 231, 221, 1)"),
    ("Zip_code", "", "rgba(248, 215, 218, 1)")
])

def test_field_highlight(browser, field_name, field_value, expected_color):
# 1. Откройте сайт магазина
    page = DatatypesPage(browser, "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# 2. Заполните форму значениями
#### В отличии от первого варианта используется getattr
#### В результате код стал гораздо короче, но для проверки каждого поля используется отдельный запуск теста
    getattr(page, f"type_{field_name}")(field_value)
     
# 3. Нажмите кнопку Submit.
    page.clk_Submit()
    
# 4. Проверьте (assert), что поле `Zip code` подсвечено красным. rgba(248, 215, 218, 1)
    assert page.bkgr_Zip_code() == "rgba(248, 215, 218, 1)"
    
# 5. Проверьте (assert), что остальные поля подсвечены зеленым. rgba(209, 231, 221, 1)
    assert getattr(page, f"bkgr_{field_name}")() == expected_color