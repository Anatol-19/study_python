from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


plus = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
equally = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
seven = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
eight = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
screen = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div')

input_l = driver.find_element(By.CSS_SELECTOR, "#delay")
input_l.clear()
input_l.send_keys(45)

def sum(delay):
    seven.click()
    plus.click()
    eight.click()
    equally.click()
    WebDriverWait(driver, delay).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))
    element = screen.get_attribute("textContent")
    return element

def test_45():
    result = sum(46)
    print(result)
    print(type(result))
    assert result == "15"