from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQLデータベース接続設定
app.config["MYSQL_HOST"] = "localhost"  # ホスト名
app.config["MYSQL_USER"] = "user"  # ユーザー名
app.config["MYSQL_PASSWORD"] = "user"  # パスワード
app.config["MYSQL_DB"] = "snow_sercher"  # データベース名
mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM weather_data")  # your_tableを実際のテーブル名に置き換える
    rows = cur.fetchall()
    cur.close()
    return render_template("index.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
