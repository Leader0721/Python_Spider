# -*- coding:utf-8 -*-
import os
import re
import requests

# 图片存放路径
FOLDER_SAVE = r'E:/Sprider/BaiduSearch'


def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        if not os.path.exists(FOLDER_SAVE):
            os.makedirs(FOLDER_SAVE)
        file_path = '%s/%s.jpg' % (FOLDER_SAVE, keyword + str(i))  # 生成图片文件名

        # if os.path.exists(file_path):  # 避免重复下载
        #     print('[exists]')
        #     return
        fp = open(file_path, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    # word = input("Input key word: ")
    word = "关羽"
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text, word)
