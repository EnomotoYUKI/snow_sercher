import threading
import time
import sensing
import dataSend
import schedule
import os


class main:
    def __init__(self , csv_dir:str):
        self.se = sensing.sensing()
        self.sd = dataSend.dataSend(csv_dir)
        self.csv_dir = csv_dir
        
    def checkTrueInCSV(self):
        with open(self.csv_dir, 'r') as file:
            for line in file:
                if "true" in line:
                    return True
        return False

    def senseAndSend(self):
        print("start sensing")
        self.se.mainSense()
        time.sleep(10)  # 必要に応じて適切な待機時間を設定
        if self.checkTrueInCSV(): # もし積雪確認したら即座に送信
            print("data send")
            self.sd.sendData()
            os.remove(self.csv_dir)

    def sendData(self):
        print("data send")
        self.sd.sendData()
        os.remove(self.csv_dir)
        
    def main(self):
        #Debug
        schedule.every(10).seconds.do(self.senseAndSend)
        schedule.every(15).seconds.do(self.sendData)
        #Operation
        #schedule.every(10).minutes.do(self.senseAndSend)
        #schedule.every(30).minutes.do(self.sensdData)
        while True:
            schedule.run_pending()
            

# インスタンス作成とmainメソッドの呼び出し
if __name__ == "__main__":
    csv_dir = "EdgeDevice/strage/data.csv"
    app = main(csv_dir)
    app.main()
