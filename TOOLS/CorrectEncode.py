# encoding: utf-8
"""
把文件夹中 格式是gb2312的txt文件  转换成utf-8
"""
import os
from os.path import join

def change_encoding():
    dest = 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata\TheTrumanShowTimeWindow'

    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if OneFileName.find('.txt') == -1:
                continue
            OneFullFileName = join(root, OneFileName)

            fr = open(OneFullFileName, 'r')
            l = fr.read().decode('gb2312', 'ignore').encode('utf-8')
            print l
            fr.close()
            fw = open(OneFullFileName, 'w')
            fw.write(l)
            fw.close()
            print OneFullFileName


if __name__ == "__main__":
    change_encoding()