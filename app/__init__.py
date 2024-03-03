from flask import Flask
from flask_restful import Resource, Api, request
from app.main import exceute, get_mutations

app = Flask(__name__)
api = Api(app)

class RESULTS(Resource):
    def get(self):
        if not request.args.get("mutation"):
          {"message": "Provide mutation"}, 400
        return exceute(request.args.get("mutation"))

class MUTATIONS(Resource):
    def get(self):
        return get_mutations()

api.add_resource(RESULTS, '/results')
api.add_resource(MUTATIONS, '/mutations')

if __name__ == '__main__':
    app.run(debug=True)
