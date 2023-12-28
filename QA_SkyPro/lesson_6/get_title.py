from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://rzd.ru"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)

current_title = driver.title

print(current_title)

driver.quit()