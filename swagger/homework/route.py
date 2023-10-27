import json

import flask

import database.handler
import database.processor

import swagger.homework.models
from swagger.homework.namespace import homework
import flask_restplus
import flask_app
import swagger.mimetype


@homework.route('/')
class GetHomeWork(flask_restplus.Resource):

    def get(self):
        result = database.processor.DataProcessor().get_homework_all()
        result = json.dumps(result, ensure_ascii=False)
        return flask_app.app.response_class(response=result, status=200, mimetype=swagger.mimetype.APP_JSON)


    @homework.expect(swagger.homework.models.HOMEWORK_TABLE)
    def post(self):
        data = flask.request.json
        for i in ['date_homework', 'group', 'item', 'homework']:
            if data.get(i) is None:
                return flask_app.app.response_class(status=400)

        database.handler.Db().insert_new_homework(data['date_homework'], data['group'], data['item'], data['homework'])
        result = {"data": data['date_homework'], 'group': data['group'], 'item': data['item'], 'homework': data['homework']}
        result = json.dumps(result, ensure_ascii=False)
        return flask_app.app.response_class(response=result, status=201, mimetype=swagger.mimetype.APP_JSON)
