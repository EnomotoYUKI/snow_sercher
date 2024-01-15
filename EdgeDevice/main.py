import threading
import time
import sensing
import dataSend


class main:
    def __init__(self):
        self.se = sensing.sensing()
        self.sd = dataSend.dataSend("EdgeDevice/storage/test.csv")

    def mainSenseLoop(self):
        # 無限ループでmainSenseを実行
        while True:
            self.se.mainSense()
            time.sleep(10)  # 必要に応じて適切な待機時間を設定

    def sendDataEvery30Min(self):
        while True:
            self.sd.sendData()
            time.sleep(1800)  # 1800秒 = 30分

    def main(self):
        # mainSenseを別スレッドで実行
        sense_thread = threading.Thread(target=self.mainSenseLoop)
        sense_thread.start()

        # sendDataを別スレッドで実行
        send_thread = threading.Thread(target=self.sendDataEvery30Min)
        send_thread.start()

        # 必要に応じてメインスレッドでの処理をここに記述


# インスタンス作成とmainメソッドの呼び出し
if __name__ == "__main__":
    app = main()
    app.main()
