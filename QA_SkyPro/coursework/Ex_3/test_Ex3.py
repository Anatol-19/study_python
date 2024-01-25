from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

def find(select):
    finder = driver.find_element(By.CSS_SELECTOR, select)
    return finder

login_field = find("#user-name")
password_field = find("#password")
login_btn = find("#login-button")

# login_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
# password_field = driver.find_element(By.CSS_SELECTOR, "#password")
# login_btn = driver.find_element(By.CSS_SELECTOR, "login-button")

login = "standard_user"
password = "secret_sauce"

# Авторизуйтесь как пользователь `standard_user`.
login_field.clear()
login_field.send_keys(login)
password_field.clear()
password_field.send_keys(password)
login_btn.click()

Backpack = find("#add-to-cart-sauce-labs-backpack")
T_Shirt = find("#add-to-cart-sauce-labs-bolt-t-shirt")
Onesie = find("#add-to-cart-sauce-labs-onesie")
cart = find(".shopping_cart_link")

# 3. Добавьте в корзину товары:
Backpack.click()
T_Shirt.click()
Onesie.click()

# 4. Перейдите в корзину.
cart.click()

Checkout = find("#checkout")
# 5. Нажмите Checkout.

Checkout.click()
# 6. Заполните форму своими данными:
#     - имя,
#     - фамилия,
#     - почтовый индекс.

name_field = find("#first-name").send_keys("Анатолий")
surname_field = find("#last-name").send_keys("Киселёв")
index_field = find("#postal-code").send_keys(236022)

# 7. Нажмите кнопку Continue.
continue_btn = find("#continue").click()

# 8. Прочитайте со страницы итоговую стоимость ( `Total` ).
total_coast = find(".summary_info_label.summary_total_label").text
print(total_coast)

# 9. Закройте браузер.

driver.quit()
# 10. Проверьте, что итоговая сумма равна **$58.29.**
def test_total():
    assert "$58.29" in total_coast