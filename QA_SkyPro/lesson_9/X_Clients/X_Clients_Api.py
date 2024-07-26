import requests
from faker import Faker

fake = Faker()

accept_head = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


def fake_employee_patch(isActive=True):
    employee_patch = {
        "lastName": fake.last_name(),
        "email": fake.unique.email(),
        "url": fake.url(),
        "phone": fake.phone_number(),
        "isActive": isActive
    }
    return employee_patch


def fake_employee(id_company):
    employee_new = {
        "id": 0,
        "firstName": fake.unique.first_name(),
        "lastName": fake.last_name(),
        "middleName": fake.last_name(),
        "companyId": int(id_company),
        "email": fake.unique.email(),
        "url": fake.url(),
        "phone": fake.phone_number()[:15],
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
        "isActive": True
    }
    return employee_new


class CompanyApi:
    def __init__(self, url):
        self.url = url

    # Авторизация
    def x_clients_auth(self, user="leyla", password="water-fairy"):
        credential = {
            "username": user,
            "password": password
        }
        response = requests.post(f'{self.url}auth/login', headers=accept_head, json=credential)
        head = {
            "x-client-token": response.json()["userToken"],
            "Content-Type": "application/json",
            "accept": "application/json"
        }
        return head

    # Список всех / активных компаний
    def get_list_companies(self, params_to_add=None):
        response = requests.get(f'{self.url}company', headers=accept_head, params=params_to_add)
        company_list = response.json()
        return company_list

    # Компания по ID
    def get_one_company(self, company_id):
        response = requests.get(f'{self.url}company/{company_id}', headers=accept_head)
        return response.json()

    # Создание новой компании
    def add_new_company(self):
        company = {
            "name": fake.company(),
            "description": fake.text()
        }
        head = self.x_clients_auth()
        response = requests.post(f'{self.url}company', headers=head, json=company)
        company["id"] = response.json()["id"]
        return company

    # Изменение компании
    def edite(self, company_id, new_name, new_descr):
        new_company = {
            "name": new_name,
            "description": new_descr
        }
        head = self.x_clients_auth()
        response = requests.patch(f'{self.url}company/{company_id}', headers=head, json=new_company)
        return response.json()

    def set_active_status(self, company_id, status=True):
        body = {
            "isActive": status
        }
        head = self.x_clients_auth()
        response = requests.patch(f'{self.url}company/status/{company_id}', headers=head, json=body)
        return response.json()

    # Удаление компании
    def delete_company(self, id_company):
        head = self.x_clients_auth()
        response = requests.get(f'{self.url}company/delete/{id_company}', headers=head)
        return response.json()

    # Список сотрудников компании
    def employee_list_active(self, id_company):
        response = requests.get(f'{self.url}employee', headers=accept_head, params={"company": id_company})
        return response

    # Новый Сотрудник
    def add_new_employee(self, employee_new):
        head = self.x_clients_auth()
        return requests.post(f'{self.url}employee', headers=head, json=employee_new)

    # Получить сотрудника по ID
    def get_employee(self, id_emp):
        response = requests.get(f'{self.url}employee/{id_emp}', headers=accept_head)
        return response

    # Изменить информацию о сотруднике
    def patch_employee(self, id_emp, employee_patch):
        head = self.x_clients_auth()
        response = requests.get(f'{self.url}employee/{id_emp}', headers=head, json=employee_patch)
        return response

    # Удалить сотрудника