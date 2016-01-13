# encoding: utf-8

import os
from os.path import join

def main() :
    dest = 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata\ShawshankTimeWindow\window\Window39.txt'

    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if OneFileName.find('.txt') == -1:
                continue
            OneFullFileName = join(root, OneFileName)

            f = open(OneFullFileName)
            l = f.read().decode('gb2312', 'ignore').encode('utf-8')  # 忽略繁体字
            print l
            print 'f'



def stringdo():
    dest = 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata\ShawshankTimeWindow\window\Window112.txt'
    # dest = 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_window_all\WindowMerge1.txt'
    f = open(dest, 'r')
    l = f.read().decode('utf-8', 'ignore').encode('utf-8')  # 忽略繁体字
    print l
    changeStringStyle_lzy(l)  #这里一定要保证l不为空


def changeStringStyle_lzy(l):
    userFeature_location = l.find('userFeature', 0)
    l = l[userFeature_location+13: -1]
    print l

    userDetail_location = l.find('detail', 0)
    while userDetail_location != -1:
        twobrace_location = l.find('}}', userDetail_location)
        userDetail = l[userDetail_location+8: twobrace_location+1]
        print userDetail
        userDetail_location = l.find('detail', twobrace_location)




if __name__ == "__main__" :
    # main()
    stringdo()