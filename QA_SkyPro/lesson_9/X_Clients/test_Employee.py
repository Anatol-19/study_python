import pytest
import jsonschema
from Config import *
from Check_Helper import Check_Helper
from X_Clients_Api import fake_employee, fake_employee_patch

ch = Check_Helper()


@pytest.fixture()
def company_id():
    company = db.create()
    id_company = company["id"]
    db.insert_new_employee(fake_employee(id_company))
    yield id_company
    db.delete_company(id_company)


# - [GET] /employee
def test_employee_list_active(company_id):
    api_response = api.employee_list_active(company_id)
    table_data = db.get_employee_by_company_id(company_id)

    assert api_response.status_code == 200, f"Expected status code 200, but got {api_response.status_code}"
    #     - проверяющие обязательность полей.
    api_data = api_response.json()

    assert len(api_data) == len(table_data), "Количество элементов в ответах API и БД не совпадает"

    for api_item in api_data:
        db_item = next((item for item in table_data if item['id'] == api_item['id']), None)
        assert db_item is not None, f"Элемент с ID {api_item['id']} не найден в ответе БД"
        ch.compare_responses(api_item, db_item)


# - [POST] /employee
def test_add_new_employee(company_id):
    employee_new = fake_employee(company_id)
    api_response = api.add_new_employee(employee_new)

    api_data = api_response.json()

    if api_response.status_code == 400 or api_response.status_code == 500:
        print(api_response.json()["message"])
    assert api_response.status_code == 201, f"Expected status code 201, but got {api_response.status_code}"

    employee_id = api_data["id"]
    table_data = db.get_employees_by_id(employee_id)

    ch.compare_responses(api_data, table_data)
    #     - проверяющие обязательность полей.
    ch.check_api_vs_data(api_data, employee_new)


# - [GET] /employee/{id}
def test_get_one_employee(company_id):
    employee_new = fake_employee(company_id)
    new_id = db.insert_new_employee(employee_new)

    api_response = api.get_employee(new_id)
    assert api_response.status_code == 200, f"Expected status code 200, but got {api_response.status_code}"
    api_data = api_response.json()
    #     - проверяющие обязательность полей.
    try:
        jsonschema.validate(instance=api_data, schema=expected_schema)
    except jsonschema.ValidationError as e:
        assert False, f"Validation error for employee {api_data}: {e}"
    ch.check_api_vs_data(api_data, employee_new)


# - [PATCH] /employee/{id}
def test_employee_patch(company_id):
    employee_new = fake_employee(company_id)
    new_id = db.insert_new_employee(employee_new)

    api_response = api.patch_employee(new_id, fake_employee_patch())
    employee_patch = api_response.json()
    assert api_response.status_code == 200, f"Expected status code 200, but got {api_response.status_code}"
    try:
        jsonschema.validate(instance=employee_patch, schema=employee_patch)
    except jsonschema.ValidationError as e:
        assert False, f"Validation error for employee {employee_patch}: {e}"
    ch.check_api_vs_data(employee_patch, employee_new)
