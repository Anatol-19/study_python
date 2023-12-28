from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "http://labirint.ru"
my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)

driver.add_cookie(my_cookie)

cookies = driver.get_cookies()
print(cookies)

driver.refresh()

driver.delete_all_cookies()

sleep(5)

driver.quit()