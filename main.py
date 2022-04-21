from flask import Flask
from flask_restful import Api,Resource
from Attack import Attack
from Stats import Stats

app = Flask(__name__)
api = Api(app)

api.add_resource(Stats, "/api/v1/stats/")
api.add_resource(Attack, "/api/v1/attack/<string:vm_id_from_user>")

if(__name__) == "__main__":
    app.run(debug=True)
