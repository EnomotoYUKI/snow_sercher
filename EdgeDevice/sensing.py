import time
import VL53L0X
import csv
import datetime
import os
from bme280 import bme280
from bme280 import bme280_i2c


class sensing:
    def __init__(self):
        # ディレクトリのパス
        self.directory = "EdgeDevice/strage"
        # ファイル名
        self.file_name = "data.csv"
        # 完全なファイルパス
        self.filename = os.path.join(self.directory, self.file_name)
        # 閾値
        self.threshold = 10
        # ディレクトリが存在しない場合は作成
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        # ファイルが存在するかどうかを確認し、存在しなければヘッダーを書き込む
        file_exists = os.path.exists(self.filename)
        if not file_exists:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)

    def measure_distance(self):
        # VL53L0Xオブジェクトを作成
        tof = VL53L0X.VL53L0X()
        # 測定を開始
        tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        distance = tof.get_distance() / 10
        return distance

    def read_bme280(self):
        # BME280の初期化
        bme280_i2c.set_default_i2c_address(0x76)
        bme280_i2c.set_default_bus(1)
        bme280.setup()

        data = bme280.read_all()
        temperature = round(data.temperature, 2)
        humidity = round(data.humidity, 2)
        return temperature, humidity

    def rapid_measurement(self):
        count = 0
        for _ in range(5):
            distance = self.measure_distance()
            print(distance)
            if distance < self.threshold:
                count += 1
            time.sleep(1)
        return count

    def mainSense(self):
        # 温度と湿度を取得
        tem, hum = self.read_bme280()
        time.sleep(3)
        # 定期的な距離測定
        distance = self.measure_distance()
        print(distance)
        dt_now = datetime.datetime.now()

        # 距離が閾値以下の場合、短い間隔での追加測定を行う
        judge = False
        if distance < self.threshold:
            count = self.rapid_measurement()
            judge = count >= 4

        # 測定結果をCSVに記録
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([judge, tem, hum, dt_now])

        time.sleep(1)  # 300秒（5分）待機 test 10s
