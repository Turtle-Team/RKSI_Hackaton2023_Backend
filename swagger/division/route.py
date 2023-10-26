import json

import flask

import database.handler
import database.processor

import swagger.division.models
from swagger.division.namespace import division
import flask_restplus
import flask_app
import swagger.mimetype


@division.route('/')
class GetDivision(flask_restplus.Resource):

    def get(self):
        result = database.processor.DataProcessor().get_division_all()
        result = json.dumps(result, ensure_ascii=False)
        return flask_app.app.response_class(response=result, status=200, mimetype=swagger.mimetype.APP_JSON)

    @division.expect(swagger.division.models.DIVISION_COLLEGE)
    def post(self):
        data = flask.request.json
        for i in ['name', 'hour_work', 'auditoria', 'floor', 'description']:
            if data.get(i) is None:
                return flask_app.app.response_class(status=400)

        database.handler.Db().insert_new_division(data['name'], data['hour_work'], data['auditoria'], data['floor'],
                                                  data['description'])
        result = {"name": data['name'], 'hour_work': data['hour_work'], 'auditoria': data['auditoria'],
                  'floor': data['floor'], "description": data['description']}
        result = json.dumps(result, ensure_ascii=False)
        return flask_app.app.response_class(response=result, status=201, mimetype=swagger.mimetype.APP_JSON)
