import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from DataTypesPage import DataTypes


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.parametrize("inpt, url", [({
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "zip-code": "",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro"
}, "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
])

def test_sub_is_green_Zip_is_red(browser, inpt, url):
    dt = DataTypes(browser)
    dt.open_page(url)
    dt.input_form(inpt)
    dt.submit_clk()

    for i in inpt:
        element_id = "#" + i
        background = browser.find_element(By.CSS_SELECTOR, element_id).value_of_css_property("background-color")
        if i != 'zip-code':
            assert background == "rgba(209, 231, 221, 1)"

    background = browser.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
    assert background == 'rgba(248, 215, 218, 1)'