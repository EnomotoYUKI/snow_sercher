import serial
import pymysql.cursors
import datetime
import random
import socket

db_ip_addr=""
ser = serial.Serial('/dev/ttyUSB0', 9600)

def read_usb():
  global temp, humid, snowfall
  in_txt=ser.readline()
  while ser.in_waiting:
    in_txt = in_txt + ser.readline()
  print("")
  print( '    Input_Text: ', in_txt )

  txt1 = in_txt.split(b':')
  txt2 = txt1[0].split(b'Temperature=')
  txt3 = txt1[1].split(b'Humidity=')
  txt4 = txt1[2].split(b'snowfall=')
  txt5 = txt4[1].split(b'\r')

  temp = float( txt2[1] )
  humid = float( txt3[1] )
  snowfall = int( txt5[0] )

def put_data_record():
  global temp, humid, snowfall
  id = socket.gethostname()
  dt = datetime.datetime.today()
  print( 'ID=%s  DateTime=%s  Temp=%.2f  Humidity=%.2f  snowfall=%d' %(id, dt, temp, humid, snowfall) )
  try:
    with connection.cursor() as cursor:
      sql = "INSERT INTO iottbl(id, dt, temp, humid, snowfall) VALUES(%s, %s, %s, %s, %s)"
      cursor.execute( sql, (id, dt, temp, humid, snowfall ))
    connection.commit()
    print("    Data commited.")
  except:
    print("DB Access Error!")

## Main
connection = pymysql.connect(host=db_ip_addr, user="iotuser", password="iput2023", db="iotdb", charset="utf8")
try:
  for count in range(10):
    read_usb()
    put_data_record()
except KeyboardInterrupt:
  pass
ser.close()
connection.close()
