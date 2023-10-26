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

    def get(self):
        result = {"type": database.handler.Db().select_doc_type()}
        return flask_app.app.response_class(response=result, status=200, mimetype=swagger.mimetype.APP_JSON)


