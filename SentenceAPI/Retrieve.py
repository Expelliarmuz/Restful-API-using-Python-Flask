from flask import jsonify, request
from flask_restful import Resource

from SentenceAPI.common import verifyPw, countTokens, retrieveData


class Retrieve(Resource):

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

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302
            }

            return jsonify(retJson)

        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)
        sentence = retrieveData(username)

        retJson = {
            "status": 200,
            "sentence": str(sentence)
        }

        return jsonify(retJson)
