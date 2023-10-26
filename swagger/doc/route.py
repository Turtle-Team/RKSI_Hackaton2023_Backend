import json

import flask

import database.handler
import database.processor

import swagger.doc.models
from swagger.doc.namespace import doc
import flask_restplus
import flask_app
import swagger.mimetype


@doc.route('/type')
class GetType(flask_restplus.Resource):

    @doc.doc(params={'token': 'token'})
    def get(self):
        data = flask.request.args
        if not data.get('token'):
                return flask_app.app.response_class(status=401)
        is_auth_user = database.handler.Db().select_user_by_token(data.get('token'))
        if is_auth_user is None:
            return flask_app.app.response_class(status=401)

        result = database.processor.DataProcessor().get_doc_type()
        return flask_app.app.response_class(response=result, status=200, mimetype=swagger.mimetype.APP_JSON)


@doc.route('/')
class NewDocs(flask_restplus.Resource):
    @doc.expect(swagger.doc.models.DOC_CREATE)
    @doc.doc(params={'token': 'token'})
    def post(self):
        data = flask.request.args
        if not data.get('token'):
                return flask_app.app.response_class(status=401)
        is_auth_user = database.handler.Db().select_user_by_token(data.get('token'))
        if is_auth_user is None:
            return flask_app.app.response_class(status=401)

        data = flask.request.json
        for i in ['type', 'fio', 'from_id', 'platform', 'description']:
            if data.get(i) is None:
                return flask_app.app.response_class(status=400)
        database.handler.Db().insert_new_doc_requests(data['type'], data['fio'], data['from_id'], data['platform'],
                                                      data['description'])
        result = {'type': data['type']}
        result.update({'fio': data['fio']})
        result.update({'from_id': data['from_id']})
        result.update({'platform': data['platform']})
        result.update({'description': data['description']})
        result = json.dumps(result, ensure_ascii=False)
        return flask_app.app.response_class(response=result, status=201, mimetype=swagger.mimetype.APP_JSON)

    @doc.doc(params={'token': 'token'})
    def get(self):
        data = flask.request.args
        if not data.get('token'):
                return flask_app.app.response_class(status=401)
        is_auth_user = database.handler.Db().select_user_by_token(data.get('token'))
        if is_auth_user is None:
            return flask_app.app.response_class(status=401)

        result = database.processor.DataProcessor().get_doc_unready()
        return flask_app.app.response_class(response=result, status=200, mimetype=swagger.mimetype.APP_JSON)

    def put(self):
        pass
