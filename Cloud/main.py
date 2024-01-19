import dataReceaved
import insertMysql
import sendEmail
import os


class main:
    def __init__(self):
        self.dr = dataReceaved.dataReceived()
        self.im = insertMysql.insertMysql()
        self.se = sendEmail.sendEmail()

    def main(self):
        while True:
            print("Waiting for data...")
            fname = self.dr.receiveData()
            snow_flag = self.im.optimizationData(fname)
            self.im.insertMysql()
            os.remove(fname)
            print("sending email...")
            if snow_flag:
                self.se.sendEmail()


if __name__ == "__main__":
    main().main()
