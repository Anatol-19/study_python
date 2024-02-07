import pytest
from string_utils import StringUtils
util = StringUtils()

@pytest.mark.parametrize ("input_string, expected_output", [
    ("skypro", "Skypro"), # Все строчные - Первая заглавная
    ("Skypro", "Skypro"), # Первая заглавная - Первая заглавная
    ("123", "123"), # числа как строка
    ("04 апреля 2023", "04 апреля 2023"), # строка с пробелами
    (" ", " "), # Строка с пробелом
    # (None), # None
    ("", "") # Пустая строка
])

def test_capitilize(input_string, expected_output):
    # Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
    rest = util.capitilize(input_string)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, expected_output", [
    ("   SkyPro", "SkyPro"), # В начале пробелы - нет пробелов
    ("SkyPro", "SkyPro"), # В начале нет пробелов - нет пробелов
    ("123", "123"), # числа как строка
    ("04 апреля 2023", "04 апреля 2023"), # строка с пробелами
    ("", ""), # Пустая строка
    (" ", ""), # Строка с пробелом
    # (None, None), # None
])
def test_trim(input_string, expected_output):
    # Принимает на вход текст и удаляет пробелы в начале, если они есть
    rest = util.trim(input_string)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, input_delimeter, expected_output", [
    ("a,b,c,d", None, ["a", "b", "c", "d"]), # Текст с разделителем ",", delimeter не указан - список корректный	
    ("1:2:3", ":", ["1", "2", "3"]), # Текст с разделителем, указанным в delimeter - список корректный
    ("gfdboiwoujuiwhjgnwfkjnjiwbnwrn", None, ["gfdboiwoujuiwhjgnwfkjnjiwbnwrn"]), # Текст без разделителя - список из 1 пункта
    ("123", ".", ["123"]), # числа как строка
    ("", "любой", ""), # Пустая строка
    (" ", " ", ""), # Строка с пробелом
    # (None, None, None) # None

])

def test_to_list(input_string, input_delimeter, expected_output):
    # Принимает на вход текст с разделителем и возвращает список строк.
    rest = util.to_list(input_string, input_delimeter)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, input_symbol, expected_output", [
    ("SkyPro", "S", True), # Символ есть - True
    ("SkyPro", "U", False), # Символа нет - False
    ("", "", False), # Пустая строка
    (" ", " ", True), # Строка с пробелом
    # (None, "g", False)# None
])

def test_contains(input_string, input_symbol, expected_output):
    # Возвращает `True`, если строка содержит искомый символ и `False` - если нет
    rest = util.contains(input_string, input_symbol)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, input_symbol, expected_output", [
    ("SkyPro", "Pro", "Sky"), # “Текст”
    ("123", "12", "3"), # “123” — числа как строка
    ("04 апреля 2023", "еля ", "04 апр2023"), # “04 апреля 2023” — строка с пробелами
    ("SkyPro", "QA Studio", "SkyPro"), # Переданной подстроки нет в строке
    ("Pro", "SkyPro", "Pro"), # Подстрока больше строки
    ("", "SkyPro", ""), # Пустая строка
    (" ", "SkyPro", " "), # Строка с пробелом
    # (None, "SkyPro", None) # None
])

def test_delete_symbol(input_string, input_symbol, expected_output):
    # Удаляет все подстроки из переданной строки
    rest = util.delete_symbol(input_string, input_symbol)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, input_symbol, expected_output", [
    ("SkyPro", "S", True), # “Текст” - начинается с заданного символа - Возвращает `True'
    ("SkyPro", "P", False), # “Текст” - НЕ начинается с заданного символа - Возвращает `False`
    ("123", "1", True), # “123” — числа как строка - начинается с заданного символа - Возвращает `True
    ("123", "9", False), # “123” — числа как строка -  НЕ начинается с заданного символа - Возвращает `False`
    ("04 апреля 2023", "0", True), # “04 апреля 2023” — строка с пробелами -  начинается с заданного символа - Возвращает `True  
    ("04 апреля 2023", "4", False), # “04 апреля 2023” — строка с пробелами - строка НЕ начинается с заданного символа - Возвращает `False` 
    ("", "", False), # Пустая строка
    (" ", " ", True), # Строка с пробелом
    # (None, "S", False), # None
])

def test_start_with(input_string, input_symbol, expected_output):
    # Возвращает `True`, если строка начинается с заданного символа и `False` - если нет 
    rest = util.starts_with(input_string, input_symbol)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, input_symbol, expected_output", [
    ("SkyPro", "o", True), # “Текст” - заканчивается с заданного символа - Возвращает `True'
    ("SkyPro", "P", False), # “Текст” - НЕ заканчивается с заданного символа - Возвращает `False`
    ("123", "3", True), # “123” — числа как строка - заканчивается с заданного символа - Возвращает `True
    ("123", "9", False), # “123” — числа как строка -  НЕ заканчивается с заданного символа - Возвращает `False`
    ("04 апреля 2023", "3", True), # “04 апреля 2023” — строка с пробелами -  заканчивается с заданного символа - Возвращает `True  
    ("04 апреля 2023", "4", False), # “04 апреля 2023” — строка с пробелами - строка НЕ заканчивается с заданного символа - Возвращает `False` 
    ("", "", False), # Пустая строка
    (" ", " ", True), # Строка с пробелом
    # (None, "S", False), # None
])

def test_end_with(input_string, input_symbol, expected_output):
    # строка заканчивается заданным символом - Возвращает `True'
    rest = util.end_with(input_string, input_symbol)
    assert rest == expected_output

@pytest.mark.parametrize ("input_string, expected_output", [
    ("", True), # Пустая строка - Возвращает True
    (" ", True), # с 1 пробелом - Возвращает True
    ("        ", True), # с 2-3 пробелами - Возвращает True
    # (None, True), # None - Возвращает True
    ("S", False), # 1 символ - Возвращает False
    ("Тест", False), # "Тест" — не пустая строка - Возвращает False
    ("123", False), # 123 — числа как строка - Возвращает False
    ("04 апреля 2023", False), # "04 апреля 2023" — строка с пробелами -  - Возвращает False
]) 

def test_is_empty(input_string, expected_output):
    # Возвращает `True`, если строка пустая и `False` - если нет
    rest = util.is_empty(input_string)
    assert rest == expected_output

@pytest.mark.parametrize ("input_lst, input_joiner, expected_output", [
    ([1,2,3,4], "", "1, 2, 3, 4"), # Список и не указан разделитель - Преобразует список элементов в строку
    (["Sky", "Pro"], "-", "Sky-Pro"), # Список и разделитель - Преобразует список элементов в строку с указанным разделителем
    # ([], None, ""), # Пустой список — [ ] станет ""
    ([" ", " ", " "], "", "   "), # Список с пробелами — строка с пробелами
])

def test_to_string(input_lst, input_joiner, expected_output):
    # Преобразует список элементов в строку с указанным разделителем
    rest = util.list_to_string(input_lst, input_joiner)
    assert rest == expected_output
