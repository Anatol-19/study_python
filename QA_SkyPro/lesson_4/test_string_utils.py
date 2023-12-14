from string_utils import StringUtils



####### Список проверяемых опций с описанием их JTBD: #######
#### 1. capitilize(self, string: str) -> str:
#         """
#         Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
#         Пример: `capitilize("skypro") -> "Skypro"`
#         """
#     
#### 2. trim(self, string: str) -> str:
#         """
#         Принимает на вход текст и удаляет пробелы в начале, если они есть
#         Пример: `trim("   skypro") -> "skypro"`
#         """
#     
#### 3. to_list(self, string: str, delimeter = ",") -> list[str]:
#         """
#         Принимает на вход текст с разделителем и возвращает список строк. \n
#         Параметры: \n 
#             `string` - строка для обработки \n
#             `delimeter` - разделитель строк. По умолчанию запятая (",") \n
#         Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
#         Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
#         """
#     
#### 4. contains(self, string: str, symbol: str) -> bool:
#         """
#         Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
#         Параметры: \n 
#             `string` - строка для обработки \n
#             `symbol` - искомый символ \n
#         Пример 1: `contains("SkyPro", "S") -> True`
#         Пример 2: `contains("SkyPro", "U") -> False`
#         """
#     
#### 5. delete_symbol(self, string: str, symbol: str) -> str:
#         """
#         Удаляет все подстроки из переданной строки \n 
#         Параметры: \n 
#             `string` - строка для обработки \n
#             `symbol` - искомый символ для удаления \n
#         Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
#         Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
#         """
#     
#### 6. def starts_with(self, string: str, symbol: str) -> bool:
#         """
#         Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
#         Параметры: \n 
#             `string` - строка для обработки \n
#             `symbol` - искомый символ \n
#         Пример 1: `starts_with("SkyPro", "S") -> True`
#         Пример 2: `starts_with("SkyPro", "P") -> False`
#         """
#
#### 7. end_with(self, string: str, symbol: str) -> bool:
#         """
#         Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
#         Параметры: \n 
#             `string` - строка для обработки \n
#             `symbol` - искомый символ \n
#         Пример 1: `end_with("SkyPro", "o") -> True`
#         Пример 2: `end_with("SkyPro", "y") -> False`
#         """
#   
#### 8. is_empty(self, string: str) -> bool:
#         """
#         Возвращает `True`, если строка пустая и `False` - если нет \n 
#         Пример 1: `is_empty("") -> True`
#         Пример 2: `is_empty(" ") -> True`
#         Пример 3: `is_empty("SkyPro") -> False`
#         """
#     
#### 9. list_to_string(self, lst: list, joiner=", ") -> str:
#         """
#         Преобразует список элементов в строку с указанным разделителем \n 
#         Параметры: \n 
#             `lst` - список элементов \n
#             `joiner` - разделитель элементов в строке. По умолчанию запятая (", ") \n
#         Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
#         Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
#         Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
#         """