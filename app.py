from flask import *
from flask_cors import CORS, cross_origin
from hardwareSet import HWSet
from pymongo import MongoClient
import certifi

app = Flask(__name__)
CORS(app, support_credentials=True)

client = MongoClient("mongodb+srv://abigailhu2000:Abby2000325@cluster0.rbxf8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client["Final_Project"]
HWSets = db["HWSets"]
Projects = db["Projects"]

HWSet1 = HWSet(1, HWSets.find_one({"Name" : "HWSet1"})["Capacity"])
HWSet2 = HWSet(2, HWSets.find_one({"Name" : "HWSet2"})["Capacity"])

# Add userid and project id data in req for both
@app.route('/hardware', methods=["POST"])
@cross_origin(supports_credentials=True)
def checkout1(qty: int, proj: str, hwset: int):
    if (qty == 0):
        return {"success" : False}

    if not (Projects.find_one({"projectname" : proj})):
        return {"success" : False}

    if (hwset == 1):
        res = HWSet1.check_out(qty)
        if (res == -1):
            return {"success" : False}
        else:
            return {"success" : True, "amount" : qty}
    elif (hwset == 2):
        res = HWSet2.check_out(qty)
        if (res == -1):
            return {"success" : False}
        else:
            return {"success" : "True", "amount" : qty}

if __name__ == "__main__":
    app.run(debug=True)