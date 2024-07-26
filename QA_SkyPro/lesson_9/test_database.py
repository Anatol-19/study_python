from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"


def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[1] == 'company'


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute('select * from company').fetchall()
    row1 = rows[-1]

    assert row1["id"] == 115


def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text('select * from company where id = :company_id')

    rows = db.execute(sql_statement, company_id=115).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == ""