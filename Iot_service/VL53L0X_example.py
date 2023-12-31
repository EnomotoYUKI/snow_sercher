#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X
import cv2
import numpy as np

#黒画像800x600を作成
img = np.zeros((600, 800, 3), np.uint8)
img_disp = img.copy() #img_dispにimgをコピー

# Create a VL53L0X object
tof = VL53L0X.VL53L0X()

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

# 連続測定するときに必要な時間間隔を得る
timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

while True:
    #黒画でキーが押されたら終了
    key = cv2.waitKey(1)
    if key != -1:
        break

    #必要な時間間隔を空けてから距離をcm単位にして取得
    time.sleep(timing/1000000.00)
    distance = tof.get_distance()/10
    text = str(distance) + 'cm'

    #黒画に距離の文字列を描画
    img_disp = img.copy() #img_dispにimgをコピー
    cv2.putText(img_disp, text, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 16)
    cv2.imshow('black', img_disp)

#終了処理
tof.stop_ranging()
cv2.destroyAllWindows()