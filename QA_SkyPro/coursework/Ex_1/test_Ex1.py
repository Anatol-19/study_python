from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

variable = {
    "first-name" : "Иван",
    "last-name" : "Петров",
    "address" : "Ленина, 55-3",
    "e-mail" : "test@skypro.com",
    "phone" : "+7985899998787",
    "zip-code" : "",
    "city" : "Москва",
    "country" : "Россия",
    "job-position" : "QA",
    "company" : "SkyPro"
}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

for i in variable:
    element = driver.find_element(By.NAME, i)
    element.clear()
    element.send_keys(variable[i])

submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']")

submit.click()

def test_sub_is_green():
    for i in variable:
        element_id = "#" + i
        background = driver.find_element(By.CSS_SELECTOR, element_id).value_of_css_property("background-color")
        if i != 'zip-code':
            assert background == "rgba(209, 231, 221, 1)"

sleep(1)

def test_Zip_is_red():
    background = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
    assert background == 'rgba(248, 215, 218, 1)'

# driver.quit()
