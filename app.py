from flask import Flask, request
from flask_cors import CORS, cross_origin
from hardwareSet import HWSet
from pymongo import MongoClient
import certifi
import sys

app = Flask(__name__)
CORS(app, support_credentials=True)

client = MongoClient("mongodb+srv://abigailhu2000:Abby2000325@cluster0.rbxf8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client["Final_Project"]
HWSets = db["HWSets"]
Projects = db["Projects"]

HWSet1 = HWSet(1, HWSets.find_one({"Name" : "HWSet1"})["Capacity"])
HWSet2 = HWSet(2, HWSets.find_one({"Name" : "HWSet2"})["Capacity"])

# Add userid and project id data in req for both
@app.route('/hardware', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def checkout():
    data = request.get_json()
    if (data.get("qty") == 0):
        return {"success" : False}

    if not (Projects.find_one({"projectname" : data.get("proj")})):
        return {"success" : False}

    if (data.get("hwset") == "1"):
        res = HWSet1.check_out(data.get("qty"))
        if (res == -1):
            return {"success" : False}
        else:
            return {"success" : True, "amount" : data.get("qty")}
    elif (data.get("hwset") == "2"):
        res = HWSet2.check_out(data.get("qty"))
        if (res == -1):
            return {"success" : False}
        else:
            return {"success" : True, "amount" : data.get("qty")}

if __name__ == "__main__":
    app.run(debug=True)