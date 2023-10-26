import json
import database.handler
import database.obj
import hashlib
import random

class DataProcessor:
    @staticmethod
    def get_user(token):
        json_data = {'result': None}
        handler = database.handler.Db()

        result = handler.select_user_by_token(token)
        if result is not None and len(result) > 0:
            result = handler.select_user_by_login(result[0])
            json_data = {'id': result[0], 'login': result[1]}
        return json.dumps(json_data)

    @staticmethod
    def auth_user(login: str, password: str):
        handler = database.handler.Db()
        hash = None
        if handler.select_user_from_log_pass(login, password):
            hash = hashlib.sha256(str(str(random.randint(0, 999999999999)) + login).encode()).hexdigest()
        handler.clear_tokens(login)
        handler.insert_new_token(login, hash)
        return hash

    def is_auth(self, token):
        if len(database.handler.Db().select_user_by_token(token)) > 0:
            return True
        return False

    def get_division_all(self):
        divisions = []
        for i in database.handler.Db().select_division_all():
            divisions.append(database.obj.Division(*i).to_dict())
        return divisions

    def get_doc_type(self):
        result = []
        for i in database.handler.Db().select_doc_type():
            result.append({"id": i[0], 'name': i[1]})
        return json.dumps(result, ensure_ascii=False)

    def get_doc_unready(self):
        result = []
        for i in database.handler.Db().select_doc_dont_ready():
            # result.append({"id": i[0], 'type': i[1], 'fio': i[2], 'from_id': i[3], 'platform': i[4], 'description': i[5], 'is_ready': i[6]})
            result.append(database.obj.DocRequest(*i).to_dict())
        return json.dumps(result, ensure_ascii=False)
