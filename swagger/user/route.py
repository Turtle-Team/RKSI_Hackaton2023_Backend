import hashlib
import json

import flask

import database.handler
import database.processor

import swagger.user.models
from swagger.user.namespace import user
import flask_restplus
import flask_app
import swagger.mimetype


@user.route('/new', methods=['POST'])
class NewUser(flask_restplus.Resource):

    @user.expect(swagger.user.models.AUTH_USER)
    def post(self):
        data = flask.request.json
        if not data.get('login') or not data.get('password'):
            return flask_app.app.response_class(status=400)
        password = hashlib.sha256(data.get('password').encode()).hexdigest()
        status_code = 200 if database.handler.Db().new_user(data.get('login'), password) else 409
        return flask_app.app.response_class(status=status_code)

@user.route('/auth', methods=['GET'])
class AuthUser(flask_restplus.Resource):
    @user.doc(params={'login': 'login', 'password': 'pass'})
    def get(self):
        mimetype = swagger.mimetype.APP_JSON
        status_code = 200
        data = flask.request.args
        if not data.get('login') or not data.get('password'):
            return flask_app.app.response_class(status=400)
        password = hashlib.sha256(data.get('password').encode()).hexdigest()
        token = database.processor.DataProcessor().auth_user(data.get('login'), password)
        result = {"token": token}
        if token is None:
            status_code = 401
        result = json.dumps(result, ensure_ascii=True)
        return flask_app.app.response_class(status=status_code, response=result, mimetype=mimetype)

@user.route('/get', methods=['GET'])
class GetUser(flask_restplus.Resource):
    @user.doc(params={'token': 'token'})
    def get(self):
        mimetype = swagger.mimetype.APP_JSON
        status_code = 200
        data = flask.request.args
        if not data.get('token'):
            return flask_app.app.response_class(status=401)
        result = database.processor.DataProcessor().get_user(data.get('token'))
        return flask_app.app.response_class(response=result, status=status_code, mimetype=mimetype)

@user.route('/totp', methods=['GET'])
class UserTotp(flask_restplus.Resource):
    @user.expect()
    def get(self):
        data = flask.request.json
        if not data.get('login') or not data.get('password'):
            return flask_app.app.response_class(status=400)
        password = hashlib.sha256(data.get('password')).hexdigest()
        status_code = 200 if database.handler.Db().new_user(data.get('login'), password) else 409
        return flask_app.app.response_class(status=status_code)
