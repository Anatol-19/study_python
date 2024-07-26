from sqlalchemy import create_engine
from sqlalchemy.sql import text
from faker import Faker
from Check_Helper import Check_Helper
from X_Clients_Api import fake_employee

fake = Faker()
ch = Check_Helper()


class CompanyTable:
    __scripts = {
        "select": "select * from company",
        "select by id": text("select * from company where id = :company_id"),
        "select only active": "select * from company where \"is_active\" = true",
        "delete by id": text("delete from company where id = :id_to_delete"),
        "delete employees by company id": text("delete from employee where \"company_id\" = :company_id"),
        "insert new": text("insert into company(\"name\", \"description\") values (:new_name, :new_description)"),
        "get max id": "select MAX(id) from company",
        "get id company by name": text("select * from company where \"name\" = :company_name"),
        "select employee by company id": text("select * from employee where \"company_id\" = :company_id"),
        "select employee by id": text("select * from employee where \"id\" = :employee_id"),
        "insert new employee": text(
            "insert into employee(\"is_active\", \"create_timestamp\", \"change_timestamp\", \"first_name\", \"last_name\", \"phone\", \"email\", \"company_id\") values (true, now(), now(), :first_name, :last_name, :phone_number, :email, :company_id) returning ID")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select only active"]).fetchall()

    def get_company_by_id(self, company_id):
        return self.__db.execute(self.__scripts["select by id"], company_id=company_id).fetchall()

    def delete_company(self, company_id):
        self.delete_employees_by_company_id(company_id)
        self.__db.execute(self.__scripts["delete by id"], id_to_delete=company_id)

    def delete_employees_by_company_id(self, company_id):
        self.__db.execute(self.__scripts["delete employees by company id"], company_id=company_id)

    def create(self):
        company = {
            "name": fake.company(),
            "description": fake.text()
        }
        self.__db.execute(self.__scripts["insert new"], new_name=company["name"],
                          new_description=company["description"])
        company["id"] = \
            self.__db.execute(self.__scripts["get id company by name"], company_name=company["name"]).fetchall()[0][
                'id']
        return company

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def get_employee_by_company_id(self, company_id):
        # return self.__db.execute(self.__scripts["select employee by company id"], company_id=company_id).fetchall()
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select employee by company id"], company_id=company_id)
            rows = result.fetchall()
            column_names = list(result.keys())
            return ch.transform_db_response(rows, column_names)

    def get_employees_by_id(self, employee_id):
        with self.__db.connect() as conn:
            result = conn.execute(self.__scripts["select employee by id"], employee_id=employee_id)
            rows = result.fetchall()
            column_names = list(result.keys())
            return ch.transform_db_response(rows, column_names)

    def insert_new_employee(self, new):
        my_params = {
            "first_name": new["firstName"],
            "last_name": new["lastName"],
            "phone_number": new["phone"],
            "email": new["email"],
            "company_id": new["companyId"]
        }
        return self.__db.execute(self.__scripts["insert new employee"], my_params).fetchall()
