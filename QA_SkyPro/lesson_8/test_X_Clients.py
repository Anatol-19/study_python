import requests

base_url = "https://x-clients-be.onrender.com/"

credentional = {
    "username": "roxy",
    "password": "animal-fairy"
}
# **Задание. Напишите автотесты на методы приложения x-clients.** 

def test_auth():
    response = requests.post(f'{base_url}auth/login', json=credentional)
    token = response["userToken"]
    assert response.status_code(201)
    return token

# - [GET] /employee
# - [POST] /employee
# - [GET] /employee/{id}
# - [PATCH] /employee/{id}
# 4. Тесты должны быть двух видов:
#     - позитивные,
#     - проверяющие обязательность полей.