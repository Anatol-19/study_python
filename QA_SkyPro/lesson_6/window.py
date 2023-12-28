from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://ya.ru"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)

driver.maximize_window()
sleep(1)
driver.minimize_window()
sleep(1)
driver.fullscreen_window()
sleep(1)
driver.set_window_size(1200, 800)
sleep(2)
driver.quit()