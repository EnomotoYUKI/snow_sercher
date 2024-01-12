from flask import Flask, request, jsonify
import insertMysql
import sendEmail

app = Flask(__name__)

@app.route('/submit_data', methods=['POST'])
def receive_data():
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    snow_depth = data.get('snow_depth')  # True または False

    # ここでデータを処理（例：データベースへの保存、アラートのチェックなど）
    print(f"受け取ったデータ: 温度={temperature}, 湿度={humidity}, 積雪量={snow_depth}")

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
