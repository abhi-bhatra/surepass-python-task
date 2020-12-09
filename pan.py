from flask import Flask, jsonify
from flask_restx import Api, Resource, reqparse, abort
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from flask.json import JSONEncoder
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from datetime import date

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
app.config['JSON_SORT_KEYS'] = False
db = MongoEngine(app)
jwt = JWTManager(app)
api = Api(app)

class BackendError(Exception):
    pass
    # abort(400, custom='Oop! Something went wrong!!!')

@api.route('/<string:pan_number>')
class Sample(Resource):
    # data = parser.parse_args()
    def get(self, pan_number):
        testdate = date(1990,10,25)
        access_token = create_access_token(identity = pan_number)
        return jsonify({
            'pan': pan_number,
            'name': 'Dinesh Kumar',
            'dob': testdate,
            'father_name': 'Hari Kumar',
            'client_id': access_token
        })

api.add_resource(Sample, '/<string:pan_number>', endpoint='pan_number_ep')

if __name__ == '__main__':
    app.run(debug=True)
