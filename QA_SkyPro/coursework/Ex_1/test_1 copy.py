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

sleep(1)

for i in variable:
    id = "#" + i
    print(id)
    background = driver.find_element(By.CSS_SELECTOR, i).value_of_css_property("background-color")
    if i != 'zip-code':
        assert background == "rgb(209, 231, 221)"
    else:
        assert background == 'rgb(245, 194, 199)'
    # print(f'{i} {background}')

driver.quit()

