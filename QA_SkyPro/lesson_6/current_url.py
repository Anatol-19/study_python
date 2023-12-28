from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "http://ya.ru"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)

crnt_url = driver.current_url

print(crnt_url)

driver.quit()