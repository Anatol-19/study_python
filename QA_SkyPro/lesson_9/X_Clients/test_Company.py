from Config import *


# Методы из урока
def test_get_companies():
    api_result = api.get_list_companies()
    db_result = db.get_companies()
    assert len(api_result) != len(db_result)


def test_get_active_companies():
    filtered_list = api.get_list_companies({'active': 'true'})
    db_list = db.get_active_companies()
    assert len(filtered_list) != len(db_list)


def test_add_new_company():
    body = api.get_list_companies()
    len_before = len(body)

    company = api.add_new_company()

    body = api.get_list_companies()
    len_after = len(body)

    db.delete_company(company["id"])

    assert len_after - len_before == 1
    for company in body:
        if company["id"] == company["id"]:
            assert company["name"] == company["name"]
            assert company["id"] == company["id"]
            assert company["description"] == company["description"]


def test_get_one_company():
    company = db.create()
    company_id = company["id"]

    new_company = api.get_one_company(company_id)

    db.delete_company(company_id)

    assert new_company["id"] == company_id
    assert new_company["name"] == company["name"]
    assert new_company["description"] == company["description"]
    assert new_company["isActive"] is True


def test_edit():
    company = db.create()
    company_id = company["id"]

    new_name = "UPDATED"
    new_descr = "__upd__"
    edited = api.edite(company_id, new_name, new_descr)

    db.delete_company(company_id)

    assert edited["id"] == company_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] is True


def test_delete():
    company = db.create()
    company_id = company["id"]

    deleted = api.delete_company(company_id)
    assert deleted["id"] == company_id
    assert deleted["name"] == company["name"]
    assert deleted["description"] == company["description"]
    assert deleted["isActive"] is True

    rows = db.get_company_by_id(company_id)
    body = api.get_list_companies()

    assert body[-1]["id"] != company_id
    assert len(rows) == 0
    # assert rows[0]["deleted_at"] is not None
    # ToDo Дебаг проверки удаления


def test_deactivate():
    company = db.create()
    company_id = company["id"]

    body = api.set_active_status(company_id, False)
    assert body["isActive"] is False

    body = api.set_active_status(company_id, True)
    assert body["isActive"] is True

    db.delete_company(company_id)