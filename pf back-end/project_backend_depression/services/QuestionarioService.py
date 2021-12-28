import sys
import pathlib
import json
from connection.Connection import Connection

# Retorna o caminho absoluto do projeto, para facilitar a implementação em outros sistemas
sys.path.append(r'' + str(pathlib.Path().absolute()))


class QuestionarioService(Connection):

    def inserir(self, data):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO resultados VALUES (NULL, %s,%s,%s,%s,%s)", data)
            self.connection.commit()
            if cursor.rowcount > 1:
                return 0
            return 1
        except:
            return 0

    def selecioanar(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM resultados")
            self.connection.commit()
            result = cursor.fetchall()
            array_data = dict()
            for data in result:
                array_data.update({
                    data[0]: {
                        "nome_usuario": data[1],
                        "idade_usuario": data[2],
                        "email_usuario": data[3],
                        "pontuacao": int(data[4]),
                        "resultado": data[5]
                    }
                })
            return json.dumps({
                "content": [
                    array_data
                ]
            })
        except:
            return 0
