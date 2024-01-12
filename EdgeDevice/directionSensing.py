import time
import Iot_service.VL53L0X as VL53L0X
import csv
import datetime
import os

# CSVファイル名
filename = 'data.csv'
# ファイルが存在するかどうかを確認し、存在しなければヘッダーを書き込む
file_exists = os.path.exists(filename)
if not file_exists:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Judge', 'Temperature', 'Humidity', 'Datetime'])

# VL53L0Xオブジェクトを作成
tof = VL53L0X.VL53L0X()
# 測定を開始
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

# 閾値
threshold = 10

def measure_distance():
    distance = tof.get_distance() / 10
    return distance

def rapid_measurement(threshold):
    count = 0
    for _ in range(5):
        distance = measure_distance()
        if distance < threshold:
            count += 1
        time.sleep(3)
    return count

# 主ループ
while True:
    # 定期的な測定
    distance = measure_distance()
    tem = 0  # 温度センサからの読み取りを実装する
    hum = 0  # 湿度センサからの読み取りを実装する
    dt_now = datetime.datetime.now()

    # 距離が閾値以下の場合、短い間隔での追加測定を行う
    judge = False
    if distance < threshold:
        count = rapid_measurement(threshold)
        judge = count >= 4

    # 測定結果をCSVに記録
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([judge, tem, hum, dt_now])

    time.sleep(10)  # 300秒（5分）待機

# 終了処理
tof.stop_ranging()
