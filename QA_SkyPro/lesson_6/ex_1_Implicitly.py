from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "http://uitestingplayground.com/ajax"

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# в терминале выводится ошибка SSL из DevTools
# DevTools listening on ws://127.0.0.1:60145/devtools/browser/713e3bda-c4ea-4c48-8bb2-0fad5f9e7ab4
# [17632:17220:0114/170322.035:ERROR:ssl_client_socket_impl.cc(975)] handshake failed; returned -1, SSL error code 1, net_error -200

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.implicitly_wait(25)

driver.get(url)

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(f'В поле значение - "{txt}"')
driver.quit()