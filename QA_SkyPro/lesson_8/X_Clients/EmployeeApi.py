import requests
from faker import Faker

fake = Faker()
# ToDo Пересмотреть реализайциии методов после создания тестовой компании в рамках фикстуры

class EmployeeApi:
    def __init__(self, url):
        self.url = url

    ## Авторизация
    def x_clients_auth(self, user="leyla", password="water-fairy"):
        credentional = {
            "username": user,
            "password": password
        }
        response = requests.post(f'{self.url}auth/login', json=credentional)
        head = {
            "x-client-token": response.json()["userToken"],
            "Content-Type": "application/json",
            "accept": "application/json"
        }
        return head

    ## Список активных компаний
    def get_list_company(self, params_to_add=None):
        response = requests.get(f'{self.url}company', params=params_to_add)
        company_list = response.json()
        return company_list

    ## Создание новой компании
    def add_new_company(self):
        company = {
            "name": fake.company(),
            "description": fake.text()
        }
        head = self.x_clients_auth()
        response = requests.post(f'{self.url}company', headers=head, json=company)
        return response.json()["id"]

    ## Удаление комании
    # ToDo Реализовать метод
    def delete_company(self, id_company):
        pass

    ## Список сотрудников компании
    def employee_list_active(self, Nomber_of_Company=0):
        id_comp = str(self.get_list_company({'active': 'true'})[Nomber_of_Company]['id'])
        response = requests.get(f'{self.url}employee', params={"company": id_comp})
        return response

    ## Новый Сотрудник
    def add_new_employee(self, id_company):
        head = self.x_clients_auth()
        # id_company = self.add_new_company()
        employee_new = {
            "id": 0,
            "firstName": fake.unique.first_name(),
            "lastName": fake.last_name(),
            "middleName": fake.last_name(),
            "companyId": id_company,
            "email": fake.unique.email(),
            "url": fake.url(),
            "phone": fake.phone_number(),
            "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
            "isActive": True
        }
        return requests.post(f'{self.url}employee', headers=head, json=employee_new)

    ## Получить сотрудника по ID
    def get_employee(self, id_emp):
        response = requests.get(f'{self.url}employee/{id_emp}')
        return response

    ## Изменить информацию о сотруднике
    def patch_employee(self, id_emp, isActive=True):
        head = self.x_clients_auth()
        employee_patch = {
            "lastName": fake.last_name(),
            "email": fake.unique.email(),
            "url": fake.url(),
            "phone": fake.phone_number(),
            "isActive": isActive
        }
        response = requests.get(f'{self.url}employee/{id_emp}', headers=head, json=employee_patch)
        return response

