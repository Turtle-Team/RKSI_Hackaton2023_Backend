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
        status_code = 200 if database.handler.Db().new_user(data.get('login'), data.get('password')) else 409
        return flask_app.app.response_class(status=status_code)
