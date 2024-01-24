from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

plus = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')

# Авторизуйтесь как пользователь `standard_user`.
# 3. Добавьте в корзину товары:
#     - Sauce Labs Backpack
#     - Sauce Labs Bolt T-Shirt
#     - Sauce Labs Onesie
# 4. Перейдите в корзину.
# 5. Нажмите Checkout.
# 6. Заполните форму своими данными:
#     - имя,
#     - фамилия,
#     - почтовый индекс.
# 7. Нажмите кнопку Continue.
# 8. Прочитайте со страницы итоговую стоимость ( `Total` ).
# 9. Закройте браузер.
# 10. Проверьте, что итоговая сумма равна **$58.29.**