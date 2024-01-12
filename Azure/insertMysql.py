import mysql.connector as mydb
import os
from dotenv import load_dotenv

class insertMysql:
    
    def __init__(self):
        load_dotenv()

    def insertMysql( self , data):
        conn = mydb.connector.connect(
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            database=os.environ['DB_DATABASE']
        )
