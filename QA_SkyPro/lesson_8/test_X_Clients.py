import requests
from EmployeeApi import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com/")
   
# **Задание. Напишите автотесты на методы приложения x-clients.** 
# - [GET] /employee
def test_employee_list_active(Nomber_of_Company = 0):
    response = api.employee_list_active(Nomber_of_Company)
    assert response.status_code == 200
#     - проверяющие обязательность полей.

# - [POST] /employee
def test_add_new_employee(Nomber_of_Company = -1):
    body = api.employee_list_active(Nomber_of_Company).json()
    len_before = len(body)

    response = api.add_new_employee(Nomber_of_Company)

    body = api.employee_list_active(Nomber_of_Company).json()
    len_after = len(body)
    assert response.status_code == 201
    assert len_after == len_before + 1
#     - проверяющие обязательность полей.

# - [GET] /employee/{id}
def test_get_one_employee(Nomber_of_Company = 0):
    result = api.add_new_employee(Nomber_of_Company).json()
    new_id = result["id"]
    new_employee = api.get_employee(new_id)
    assert new_employee.status_code == 200
    assert new_employee.json()["id"] == new_id
#     - проверяющие обязательность полей.

# - [PATCH] /employee/{id}
def test_employee_patch(Nomber_of_Company = 1):
    result = api.add_new_employee(Nomber_of_Company).json()
    new_id = result["id"]
    patch_employee = api.patch_employee(new_id)
    assert patch_employee.status_code == 200
    # assert patch_employee.json()["id"] == new_id
#     - проверяющие обязательность полей.
