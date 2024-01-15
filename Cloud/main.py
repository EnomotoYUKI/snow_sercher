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
            fname = self.dr.receiveData()
            snow_flag = self.im.optimizationData(fname)
            self.im.insertMysql()
            os.remove(fname)
            
            if(snow_flag):
                self.se.sendEmail()
            print("loop finish")
                
if __name__ == '__main__':
    main().main()
            
            
            