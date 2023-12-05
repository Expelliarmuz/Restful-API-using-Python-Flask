from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import bcrypt

from SentenceAPI.Store import  Store
from SentenceAPI.Retrieve import Retrieve
from SentenceAPI.common import insertData

app = Flask(__name__)
api = Api(app)


class Register(Resource):
    def get(self):
        # code for GET request here
        pass

    def post(self):
        # code for POST request here
        pass

    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        insertData(username,hashed_pw)

        retJson = {
            "Status": 200,
            "msg": "You have successfully signed up for our API"
        }
        return jsonify(retJson)


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Retrieve, '/retrieve')

if __name__ == "__main__":
    app.run(debug=True)
