import sys
import pathlib
from typing_extensions import Required
from services.QuestionarioService import QuestionarioService
from flask_restful import Resource, reqparse
sys.path.append(r'' + str(pathlib.Path().absolute()))


class QuestionarioInsertRoute(Resource):

    def post(self):
        try:
            param = reqparse.RequestParser()
            param.add_argument('nome', type=str, required=False)
            param.add_argument('idade', type=int, required=False)
            param.add_argument('email', type=str, required=False)
            param.add_argument('pontuacao', type=int,
                               required=True, help="Informe a pontuação")
            param.add_argument('resultado', type=str, required=True,
                               help="É necessário informar o resultado")

            args = param.parse_args()
            data = (args["nome"], args["idade"], args["email"],
                    args["pontuacao"], args["resultado"])

            questionario = QuestionarioService()
            result = questionario.inserir(data)

            if result == 0:
                return {
                    "error": "Erro ao executar inserção de dados. Consulte os logs do SQL para mais detalhes"
                }, 400

            return {
                "message": "Inserido com sucesso"
            }, 201
        except:
            return {
                "error": "Erro ao inserir dados. Contate o administrador para mais detalhes"
            }, 500
