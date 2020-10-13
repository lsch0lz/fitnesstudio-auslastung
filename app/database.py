"""import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
connection = mysql.connector.connect(
        host = 'dd47114',
        database = 'Auslastung',
        user = 'd033d63a',
        password = 'XDJEtEeKkvnRkb7u')
try:


    mySql_insert_query = INSERT INTO Auslastung (date, auslastung) VALUES (2020-01-01, 13)

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()

    print(cursor.rowcount, "A Row has been created")
    cursor.close()

except mysql.connector.Error as error:
    print("Failes {}".format(error))

finally:
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")"""

import json

from app import app, routes

with open('databse.json', 'w') as f:
    json.dump(routes.get_auslastung(), f)



