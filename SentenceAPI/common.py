from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb://localhost:27017")
db = client.sentenceDB
users = db["Users"]


def verifyPw(username, password):
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def countTokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens


def insertData(username,hashed_pw):
    return users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 6
        })


def updateData(username, sentence, num_tokens):
    return users.update_one({
        "Username": username
    },
        {
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens - 1
            }
        })

def retrieveData(username):
    return users.find({
        "Username": username
    })[0]["Sentence"]
