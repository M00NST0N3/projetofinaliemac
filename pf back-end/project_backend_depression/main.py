from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.QuestionarioRoutes import QuestionarioInsertRoute

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

api.add_resource(QuestionarioInsertRoute, "/questionario")  # POST

if __name__ == "__main__":
    app.run(port=3333, debug=True)