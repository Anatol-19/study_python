from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

variable = {
    "First name" : "Иван",
    "Last name" : "Петров",
    "Address" : "Ленина, 55-3",
    "Email" : "test@skypro.com",
    "Phone number" : "+7985899998787",
    "Zip code" : "",
    "City" : "Москва",
    "Country" : "Россия",
    "Job position" : "QA",
    "Company" : "SkyPro"
}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

f_n_str = driver.find_element(By.NAME, "first-name")
l_n_str = driver.find_element(By.NAME, "last-name")
address = driver.find_element(By.NAME, "address")
email = driver.find_element(By.NAME, "e-mail")
phone = driver.find_element(By.NAME, "phone")
zip_code = driver.find_element(By.NAME, "zip-code")
city = driver.find_element(By.NAME, "city")
country = driver.find_element(By.NAME, "country")
job_position = driver.find_element(By.NAME, "job-position")
company = driver.find_element(By.NAME, "company")
submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']")

f_n_str.clear()
f_n_str.send_keys(variable['First name'])

l_n_str.clear()
l_n_str.send_keys(variable['Last name'])

address.clear()
address.send_keys(variable['Address'])

email.clear()
email.send_keys(variable['Email'])

phone.clear()
phone.send_keys(variable['Phone number'])

zip_code.clear()
zip_code.send_keys(variable['Zip code'])

city.clear()
city.send_keys(variable['City'])

country.clear()
country.send_keys(variable['Country'])

job_position.clear()
job_position.send_keys(variable['Job position'])

company.clear()
company.send_keys(variable['Company'])

submit.click()

sleep(1)

f_n_color = driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
assert f_n_color == "rgb(209, 231, 221)"
print(f_n_color)

driver.quit()

