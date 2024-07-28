from X_Clients_Api import CompanyApi
from X_Clients_Table import CompanyTable

api = CompanyApi("https://x-clients-be.onrender.com/")
db = CompanyTable(
    "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

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
        "middleName": {"type": ["string", "null"]},
        "phone": {"type": "string"},
        "email": {"type": ["string", "null"]},
        "birthdate": {"type": ["string", "null"]},
        "avatar_url": {"type": ["string", "null"]},
        "companyId": {"type": "integer"}
    },
    "required": ["id", "firstName", "lastName", "companyId", "phone", "isActive"]
}
