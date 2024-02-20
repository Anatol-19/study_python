import pytest
from LoginPage import ShopMethods
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    # 9. Закройте браузер.
    driver.quit()

@pytest.mark.parametrize("url, login, password, f_name, l_name, zip_code", [
    ("https://www.saucedemo.com/", "standard_user", "secret_sauce", "Анатолий", "Киселёв", "236022")
    ])
def test_total(browser, url, login, password, f_name, l_name, zip_code):
    # 1. Откройте сайт магазина
    shp = ShopMethods(browser, url)
    # 2. Авторизуйтесь как пользователь `standard_user`.
    shp.authorization(login, password)
    # 3. Добавьте в корзину товары:
    shp.add_to()
    # 4. Перейдите в корзину.
    shp.go_to()
    # 5. Нажмите Checkout.
    shp.clk_check()
    # 6. Заполните форму своими данными:
    shp.input_form(f_name, l_name, zip_code)
    # 7. Нажмите кнопк у Continue.
    shp.clk_cnt()
    # 8. Прочитайте со страницы итоговую стоимость (`Total`).
    total_coast = shp.rd_total()
    # 10. Проверьте, что итоговая сумма равна **$58.29.**
    assert "$58.29" in total_coast