import mysql.connector as mydb
import os
from dotenv import load_dotenv

class insertMysql:
    
    def __init__(self):
        # .envファイルの内容を読み込みます
        load_dotenv()

    def insertMysql( self ):
        # MySQLサーバへ接続します（hostは環境変数から取得）
        conn = mydb.connect(
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            database=os.environ['DB_DATABASE_NAME'],
            port=os.environ['DB_PORT']
        )
        # 接続できているかどうか確認
        if not conn.is_connected():
            raise Exception("MySQLサーバへの接続に失敗しました")
        
        # データの書き込み
        cur = conn.cursor(dictionary=True)
        query = "INSERT INTO weather_data (temperature,humidity,snowfall) VALUES (10,10,1);"
        cur.execute(query)
        conn.commit()
        
        # 切断
        cur.close()
        conn.close()
if __name__ == '__main__':
    insertMysql().insertMysql()