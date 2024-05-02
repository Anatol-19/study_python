import requests
from ToDoAPI import SkyToDo
from faker import Faker

fake = Faker()

url = "https://todo-app-sky.herokuapp.com"

api = SkyToDo(url)

# - Создание.
def test_create_task():
    response, new_t = api.create_task()
    assert response.status_code == 201
    assert response.json()["title"] == new_t["title"]
    
# - Переименование.
def test_rename_task():
    resp1, new_t = api.create_task()
    task_url = resp1.json()["url"]
    resp2 = api.chang_title(task_url)
    assert resp2.status_code == 200
    assert resp2.json()["title"] != new_t
    
# - Удаление.
def test_delete_task():
    resp1 = api.create_task()[0]
    task_url = resp1.json()["url"]
    resp2 = api.delete_task(task_url)
    assert resp2.status_code == 204

# - Получение списка.
def test_get_list():
    response = api.get_list()
    to_do_list = response.json
    print(to_do_list)
    assert response.status_code == 200
    # assert to_do_list 
    
# - Получение конкретной задачи из списка.

# - Отметка задачи «Выполнена».

# - Снятие отметки «Выполнена».