from datetime import datetime, date


class Check_Helper:
    column_mapping = {
        'id': 'id',
        'is_active': 'isActive',
        'create_timestamp': 'createDateTime',
        'change_timestamp': 'lastChangedDateTime',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'middle_name': 'middleName',
        'phone': 'phone',
        'email': 'email',
        'birthdate': 'birthdate',
        'avatar_url': 'avatar_url',
        'company_id': 'companyId'
    }

    def __init__(self):
        pass

    def transform_db_response(self, db_response, column_names):
        transformed_response = []
        for row in db_response:
            row_dict = {column_names[i]: row[i] for i in range(len(column_names))}
            transformed_row = {api_key: row_dict[db_key] for db_key, api_key in self.column_mapping.items()}

            # Приведение типов дат к строкам в формате ISO без микросекунд
            if 'create_timestamp' in row_dict and isinstance(row_dict['create_timestamp'], datetime):
                transformed_row['createDateTime'] = row_dict['create_timestamp'].replace(microsecond=0).isoformat()
            if 'change_timestamp' in row_dict and isinstance(row_dict['change_timestamp'], datetime):
                transformed_row['lastChangedDateTime'] = row_dict['change_timestamp'].replace(microsecond=0).isoformat()
            if 'birthdate' in row_dict and isinstance(row_dict['birthdate'], date):
                transformed_row['birthdate'] = row_dict['birthdate'].isoformat()

            transformed_response.append(transformed_row)
        return transformed_response

    def compare_responses(self, api_item, db_item):
        """
        Сравнивает один элемент из ответа API с элементом из БД.
        """
        # Если db_item — список, извлекаем первый элемент
        if isinstance(db_item, list) and len(db_item) > 0:
            db_item = db_item[0]
        elif not isinstance(db_item, dict):
            raise TypeError("db_item должен быть словарем или списком словарей")

        # Сравниваем значения полей
        for key in api_item:
            api_value = api_item[key]
            db_value = db_item[key]

            # Приведение типов, если необходимо
            if isinstance(api_value, str) and isinstance(db_value, (datetime, date)):
                try:
                    # Преобразование строки API в datetime и обрезка микросекунд
                    api_value_dt = datetime.fromisoformat(api_value.replace("Z", "+00:00")).replace(microsecond=0)
                    db_value = db_value.replace(microsecond=0)
                    api_value = api_value_dt.isoformat()
                    db_value = db_value.isoformat()
                except ValueError:
                    pass
            elif isinstance(api_value, bool) and isinstance(db_value, int):
                api_value = bool(api_value)
            elif isinstance(api_value, int) and isinstance(db_value, str):
                db_value = int(db_value)

            # Приведение к строке для сравнения дат
            if isinstance(api_value, (datetime, date)):
                api_value = api_value.isoformat()
            if isinstance(db_value, (datetime, date)):
                db_value = db_value.isoformat()

            # Удаление суффиксов "Z" и "+00:00" для сравнения
            if isinstance(api_value, str):
                api_value = api_value.replace("Z", "").replace("+00:00", "")
                # Обрезка миллисекунд, если они присутствуют
                if '.' in api_value:
                    api_value = api_value.split('.')[0]
            if isinstance(db_value, str):
                db_value = db_value.replace("Z", "").replace("+00:00", "")
                # Обрезка миллисекунд, если они присутствуют
                if '.' in db_value:
                    db_value = db_value.split('.')[0]

            # Сравнение значений
            assert api_value == db_value, f"Data mismatch for ID {api_item['id']} at {key}: API = {api_value}, DB = {db_value}"

    def check_api_vs_data(self, api_response, data):
        for i in data:
            if i == "id":
                continue  # Игнорируем поле id, так как оно генерируется автоматически
            api_value = api_response.get(i)
            data_value = data[i]
            assert api_value == data_value, f"Mismatch for {i}: API = {api_value}, Data = {data_value}"
