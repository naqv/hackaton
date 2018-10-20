#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:40:36 2018

@author: natachaquintero
"""

import requests
import cv2
import numpy as np

url = "http://10.4.230.168:8080/shot.jpg"

while True:
    new_image= requests.get(url)
    img_arr= np.array(bytearray(new_image.content),dtype=np.uint8)
    img=cv2.imdecode(img_arr,-1)

    cv2.imshow("natacha",img)

    if cv2.waitKey(1)==27:
        break
