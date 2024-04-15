import pytest
from PageObject_7_2 import СalculatorPage
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
    
@pytest.mark.parametrize("delay", [
    ("45")
])

def test_Calk15(browser, delay):
# 1. Откройте страницу
    page = СalculatorPage(browser, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


# 2. В поле ввода по локатору `#delay` введите значение 45.
    page.type_Delay(delay)
    
# 3. Нажмите на кнопки:
## 7
    page.btn_seven().click()
## +
    page.btn_plus().click()
## 8
    page.btn_eight().click()
## =
    page.btn_equally().click()

# 4. Проверьте (assert), что в окне отобразится результат `15` через 45 секунд.
   
    assert page.btn_screen(delay).get_attribute("textContent") == "15"