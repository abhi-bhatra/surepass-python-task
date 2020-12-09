from flask import Flask, jsonify
from flask_restx import Api, Resource, reqparse
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from flask.json import JSONEncoder
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from datetime import date
from flask_mongoengine.wtf import model_form

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
app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': 'mongodb://localhost/database_name'
}
db = MongoEngine(app)
jwt = JWTManager(app)
api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('pan_number', help = 'This field cannot be blank', required = True)

@api.route('/<string:pan_number>')
class Sample(Resource):
    # data = parser.parse_args()
    def get(self, pan_number):
        testdate = date(1990,10,25)
        access_token = create_access_token(identity = pan_number)
        new_user = UserModel(
            pan = pan_number,
            name = 'Dinesh Kumar',
            dob = testdate,
            father_name = 'Hari Kumar',
            client_id = UserModel.generate_hash(pan_number))
        try:
            access_token = create_access_token(identity = pan_number)
            refresh_token = create_refresh_token(identity = pan_number)
            return{
                # 'pan' = pan_number,
                # 'name' = 'Dinesh Kumar',
                # 'dob' = testdate,
                # 'father_name' = 'Hari Kumar',
                'client_id': access_token
            }
        except:
            return {'message': 'Something went wrong'}, 500

class UserModel(db.Document):
    pan = db.StringField(required=True)
    name = db.StringField(max_length=50)
    dob = db.StringField(max_length=50)
    father_name = db.StringField(max_length=50)
    client_id = db.StringField(max_length=300)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

api.add_resource(Sample, '/<string:pan_number>', endpoint='pan_number_ep')
api.add_resource(UserModel,'/db', endpoint='db_ep')

if __name__ == '__main__':
    app.run(debug=True)
