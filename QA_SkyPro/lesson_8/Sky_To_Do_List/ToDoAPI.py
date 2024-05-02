import requests
from faker import Faker

fake = Faker()

url = " "
t_title = fake.text(max_nb_chars=50)

class SkyToDo:
    def __init__(self, url):
        self.url = url

#   Рандомная таска
    def random_task(self):
        new_t = {
            "title" : t_title,
            "completed" : False
        }
        return new_t
    
# - Создание.
    def create_task(self):
        new_t = self.random_task()
        response = requests.post(self.url, json = new_t)
        return response, new_t

# - Переименование
    def chang_title(self, task_url):
        new_title = { "title" : t_title }
        return requests.patch(f'{self.url}{task_url}', json = new_title)

# - Удаление.
    def delete_task(self, task_url):
        return requests.delete(f'{self.url}{task_url}')

# - Получение списка.
    def get_list(self):
        return requests.get(self.url)
    
# - Получение конкретной задачи из списка.


# - Отметка задачи «Выполнена».


# - Снятие отметки «Выполнена».
