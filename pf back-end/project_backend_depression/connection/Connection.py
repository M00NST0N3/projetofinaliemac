import mysql.connector


class Connection:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="00000",
            database="db_depre"
        )

