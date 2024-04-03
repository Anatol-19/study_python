**Задание 1. Автотест на заполнение формы** 

Напишите автотест (запускается через `pytest`). 

Шаги:

1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html.
2. Заполните форму значениями:
    
    
    | First name | Иван |
    | --- | --- |
    | Last name | Петров |
    | Address | Ленина, 55-3 |
    | Email | test@skypro.com |
    | Phone number | +7985899998787 |
    | Zip code | *оставить пустым |
    | City | Москва |
    | Country | Россия |
    | Job position | QA |
    | Company | SkyPro |
3. Нажмите кнопку Submit.
4. Проверьте (assert), что поле `Zip code` подсвечено красным.
5. Проверьте (assert), что остальные поля подсвечены зеленым.