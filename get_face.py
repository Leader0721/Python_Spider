# coding:utf-8

import urllib
import re

f = open("bilibili_user_face.txt")
line = f.readline()
# 图片存放路径
FOLDER_SAVE = r'E:/Sprider/blibli' + '/'

for i in range(1, 1000):
    print
    line,
    if re.match('http://static.*', line):
        line = f.readline()
        print
        'noface:' + str(i)
    else:
        path = FOLDER_SAVE + str(i) + ".jpg"
        data = urllib.urlretrieve(line, path)
        line = f.readline()
        print
        'succeed:' + str(i)

f.close()
