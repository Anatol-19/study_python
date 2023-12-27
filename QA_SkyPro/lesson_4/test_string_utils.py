from string_utils import StringUtils
util = StringUtils()

def test_capitilize_tc1():
    # Все строчные - Первая заглавная
    rest = util.capitilize("skypro")
    assert rest == "Skypro"

def test_capitilize_tc2():
    # Первая заглавная - Первая заглавная
    rest = util.capitilize("Skypro")
    assert rest == "Skypro"

def test_trim_tc1():
    # В начале пробелы - нет пробелов
    rest = util.trim("   SkyPro")
    assert rest == "SkyPro"

def test_trim_tc2():
    # В начале нет пробелов - нет пробелов
    rest = util.trim("SkyPro")
    assert rest == "SkyPro"

def test_list_tc1():
    # Текст с разделителем ",", delimeter не указан - список корректный
    rest = util.to_list("a,b,c,d")
    assert rest == ["a", "b", "c", "d"]   

def test_list_tc2():
    # Текст с разделителем, указанным в delimeter - список корректный
    rest = util.to_list("1:2:3", ":")
    assert rest == ["1", "2", "3"]   

def test_list_tc3():
    # Текст без разделителя - список из 1 пункта
    rest = util.to_list("gfdboiwoujuiwhjgnwfkjnjiwbnwrn")
    assert rest == ["gfdboiwoujuiwhjgnwfkjnjiwbnwrn"]

def test_contains_tc1():
    # Символ есть 
    rest = util.contains("SkyPro", "S")
    assert rest == True  

def test_contains_tc2():
    # Символа нет 
    rest = util.contains("SkyPro", "U")
    assert rest == False  

def test_delete_tc1():
    # Удаляет символ подстроки из переданной строки
    rest = util.delete_symbol("SkyPro", "k")
    assert rest == "SyPro"

def test_delete_tc2():
    # Удаляет все подстроки из переданной строки
    rest = util.delete_symbol("SkyPro", "Pro")
    assert rest == "Sky"

def test_delete_tc3():
    # Переданной подстроки нет в строке
    rest = util.delete_symbol("SkyPro", "QA Studio")
    assert rest == "SkyPro"

def test_delete_tc4():
    # Подстрока больше строки
    rest = util.delete_symbol("Pro", "SkyPro")
    assert rest == "Pro"

def test_start_tc1():
    # строка начинается с заданного символа - Возвращает `True'
    rest = util.starts_with("SkyPro", "S")
    assert rest == True

def test_start_tc2():
    # строка не начинается с заданного символа - Возвращает `False`
    rest = util.starts_with("SkyPro", "P")
    assert rest == False

def test_end_tc1():
    # строка заканчивается заданным символом - Возвращает `True'
    rest = util.end_with("SkyPro", "o")
    assert rest == True

def test_end_tc2():
    # строка не заканчивается заданным символом - Возвращает `False`
    rest = util.end_with("SkyPro", "y")
    assert rest == False

def test_empty_tc1():
    # строка пустая - Возвращает `True`
    rest = util.is_empty("")
    assert rest == True

def test_empty_tc2():
    # строка с 1 пробелом - Возвращает `True`
    rest = util.is_empty(" ")
    assert rest == True

def test_empty_tc3():
    # строка с 2-3 пробелами - Возвращает `True`
    rest = util.is_empty("        ")
    assert rest == True

def test_empty_tc4():
    # Строка не пустая - Возвращает `False`
    rest = util.is_empty("  .      ")
    assert rest == False

def test_empty_tc5():
    # Строка не пустая 1 символ - Возвращает `False`
    rest = util.is_empty("1")
    assert rest == False

def test_string_tc1():
    # Список и не указан разделитель - Преобразует список элементов в строку 
    rest = util.list_to_string([1,2,3,4])
    assert rest == "1, 2, 3, 4"
  
def test_string_tc2():
    # Список и разделитель - Преобразует список элементов в строку с указанным разделителем
    rest = util.list_to_string(["Sky", "Pro"], "-")
    assert rest == "Sky-Pro"

def test_string_tc3():
    # Пустой список станет ""
    rest = util.list_to_string([])
    assert rest == ""
