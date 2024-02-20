from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import calculator_c
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("url, wtr", [
    ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html", 45)
    ])
def test_45(browser, url, wtr):
    clk = calculator_c(browser, url)
    clk.waiter(wtr)
    result = clk.sum_15(wtr+1)
    assert result == 15