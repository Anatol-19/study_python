import requests
from faker import Faker

url = "https://todo-app-sky.herokuapp.com/"

class SkyToDo:
    def __init__(self, url):
        self.url = url

# - Создание.
    # def create_task(self):


# - Переименование.

# - Удаление.

# - Получение списка.
    def test_get_list(self):
        response = requests.get(url)
        to_do_list = response.json
        print(to_do_list)
        return response, to_do_list
    
# - Получение конкретной задачи из списка.

# - Отметка задачи «Выполнена».

# - Снятие отметки «Выполнена».