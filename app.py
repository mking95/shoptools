import datetime
import subprocess
import os
import re
import requests
from lxml import html
import pandas as pd
import cv2
import numpy as np

def save_imgurl(url):
    filename=url.split('/')[-1]
    base=url[:url.index(filename)]
    print("File: {}'\n'Base: {}".format(filename,base))
    with open(base+filename,'wb') as f:
        f.write(r.content)

def get_img(i):
    img=cv2.imread(i,0)
    w,h,c = img.shape
    print(dict(str(i)=["H":h,"W":w,"C":c]))
    return img


