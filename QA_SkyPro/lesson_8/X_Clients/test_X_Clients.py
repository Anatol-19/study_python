import pytest
import requests
from EmployeeApi import EmployeeApi
import jsonschema

api = EmployeeApi("https://x-clients-be.onrender.com/")

# Ожидаемая схема JSON
expected_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "isActive": {"type": "boolean"},
        "createDateTime": {"type": "string", "format": "date-time"},
        "lastChangedDateTime": {"type": "string", "format": "date-time"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "middleName": {"type": "string"},
        "phone": {"type": "string"},
        "email": {"type": ["string", "null"]}, 
        # "email": {"anyOf": [{"type": "string"}, {"type": "null"}]},
        "birthdate": {"type": "string", "format": "date-time"},
        "avatar_url": {"type": "string"},
        "companyId": {"type": "integer"}
    },
    "required": ["id", "firstName", "lastName", "companyId", "phone", "birthdate", "avatar_url", "isActive"]
}

@pytest.fixture()
# - перед началом теста создавать компанию, передавать её ID
def add_test_company():
    id_company = api.add_new_company()
# - Удалить её после  тестов
    yield api.delete_company(id_company)


# def add_test_company():
#     # Создаем компанию
#     id_company = api.add_new_company()
#     try:
#         # Передаем ID компании в тесты
#         yield id_company
#     finally:
#         # Удаляем компанию после завершения тестов
#         api.delete_company(id_company)


   
# **Задание. Напишите автотесты на методы приложения x-clients.** 
# - [GET] /employee
def test_employee_list_active(id_company):
    response = api.employee_list_active(id_company)
    assert response.status_code == 200
#     - проверяющие обязательность полей.
    for employee in respons
        try:
            jsonschema.validate(instance=employee, schema=expected_schema)
        except jsonschema.ValidationError as e:
            assert False, f"Validation error for employee {employee}: {e}"

# - [POST] /employee
def test_add_new_employee(id_company):
    body = api.employee_list_active(id_company).json()
    len_before = len(body)

    response = api.add_new_employee(id_company)

    body = api.employee_list_active(id_company).json()
    len_after = len(body)
    assert response.status_code == 201
    assert len_after == len_before + 1
#     - проверяющие обязательность полей.
    assert response.json()["id"] 

# - [GET] /employee/{id}
def test_get_one_employee(id_company):
    result = api.add_new_employee(id_company).json()
    new_id = result["id"]
    new_employee = api.get_employee(new_id)
    assert new_employee.status_code == 200
#     - проверяющие обязательность полей.
    try:
        jsonschema.validate(instance=new_employee.json(), schema=expected_schema)
    except jsonschema.ValidationError as e:
        assert False, f"Validation error for employee {new_employee.json()}: {e}"
    assert new_employee.json()["id"] == new_id

# - [PATCH] /employee/{id}
def test_employee_patch(id_company):
    result = api.add_new_employee(id_company).json()
    new_id = result["id"]
    response, employee_patch = api.patch_employee(new_id)
    assert response.status_code == 200
    try:
        jsonschema.validate(instance=response.json(), schema=expected_schema)
    except jsonschema.ValidationError as e:
        assert False, f"Validation error for employee {response.json()}: {e}"
    for item in employee_patch:
        assert employee_patch[item] == response.json()[item]