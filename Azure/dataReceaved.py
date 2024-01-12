from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/submit_data', methods=['POST'])
def receive_data():
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    snow_depth = data.get('snow_depth')  # True または False
    timestamp = data.get('timestamp')  # 時間データ

    # 時間データがUnixタイムスタンプ形式の場合、それを読みやすい形式に変換する
    if timestamp:
        time_received = datetime.fromtimestamp(timestamp)
    else:
        time_received = "タイムスタンプなし"

    # ここでデータを処理（例：データベースへの保存、アラートのチェックなど）
    print(f"受け取ったデータ: 時間={time_received}, 温度={temperature}, 湿度={humidity}, 積雪量={snow_depth}")

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
