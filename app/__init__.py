from flask import Flask
from flask_restful import Resource, Api, request
from app.main import Model
from click import command, option

app = Flask(__name__)
api = Api(app)

class RESULTS(Resource):
    def get(self):
        if not request.args.get("mutation"):
          {"message": "Provide mutation"}, 400
        return Model.exceute(request.args.get("mutation"))

class MUTATIONS(Resource):
    def get(self):
        return Model.get_mutations()

api.add_resource(RESULTS, '/results')
api.add_resource(MUTATIONS, '/mutations')

@app.cli.command("generate")
@option("--name", prompt="Enter mutation string")
@option("--genes")
def generate(name, genes=None):
    try:
        if genes:
            genes = genes.split(",")
        print(Model.exceute(name, genes))
    except:
        print("Invalid genes values provide a CSV value")

if __name__ == '__main__':
    app.run(debug=True)
