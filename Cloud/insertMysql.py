import mysql.connector as mydb
import os
from dotenv import load_dotenv

class insertMysql:
    
    def __init__(self):
        # .envファイルの内容を読み込みます
        load_dotenv()
        self.insertData = []

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
        
        cur = conn.cursor(dictionary=True)
        for i in self.insertData:
            # データの書き込み
            query = f"INSERT INTO weather_data (snowfall,temperature,humidity) VALUES ({i[0]},{i[1]},{i[2]});"
            cur.execute(query)
            conn.commit()
        
        # 切断
        cur.close()
        conn.close()
    def optimizationData(self,path):
        self.insertData = []
        with open(path) as f:
            for line in f:
                self.insertData.append(line.rstrip().split(","))
        print(self.insertData)
        
        
if __name__ == '__main__':
    im = insertMysql()
    im.optimizationData("./Cloud/strage/20240115052028_received.csv")
    im.insertMysql()