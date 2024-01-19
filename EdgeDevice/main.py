import threading
import time
import sensing
import dataSend
import schedule


class main:
    def __init__(self):
        self.se = sensing.sensing()
        self.sd = dataSend.dataSend("EdgeDevice/storage/test.csv")

    def senseAndSend(self):
        self.se.mainSense()
        time.sleep(10)  # 必要に応じて適切な待機時間を設定
        self.sd.sendData()
        
    def main(self):
        schedule.every(1).minutes.do(self.senseAndSend)
        while True:
            schedule.run_pending()
            

# インスタンス作成とmainメソッドの呼び出し
if __name__ == "__main__":
    app = main()
    app.main()
