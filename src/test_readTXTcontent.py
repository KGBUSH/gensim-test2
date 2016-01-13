# encoding: utf-8

"""
def data_preprocess(dest):
input:源文件夹的位置（文件夹包含n篇文档：n*.txt）
output:对两个全局变量进行赋值：list_corpora = [[(),(),()],[],[]....] ，dictionary_dy = {编号（int）: 词（str）}
"""


import os
from globalValue import *
from os.path import join
from collections import *
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities



st = "dy"
big_set = Counter()  # 把所有txt的dict放入一个大集合

big_set_newnum = Counter()

list_corpora = []  # 最后的语料库列表  [[],[],[],[],...]

# dest = "C:\Users\KGBUS\PycharmProjects\gensim-test\lzy_window_top30"

dictionary_dy = {}
# LDA中需要的dictionary：  格式为   1：“词”  注：实验发现只要语料是固定的，dictionary_dy是一个恒不变的字典

'''
def data_preprocess(dest):
    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if (OneFileName.find('.txt') == -1) or (root != dest):
                continue
            OneFullFileName = join(root, OneFileName)

            f = open(OneFullFileName)
            # l = f.read().decode('gb2312').encode('utf-8')  #这个在我的测试文件里面是正确的
            l = f.read().decode('gb2312', 'ignore').encode('utf-8')  # 忽略繁体字

            l = l[10:-1]  # 去除掉json中前后不需要的字符串
            dict_l = eval(l)
            big_set.update(dict_l)
            print dict_l
            print l
            # print dict_l.get("狙击")  #检查把字符串转化成字典是否成功

    print big_set

    big_set_newnum = big_set
    word_num = -1
    for word in big_set_newnum:
        word_num = word_num + 1
        big_set_newnum[word] = word_num
        dictionary_dy.setdefault(word_num, word)  # 编号在前面

    print "\n\n\n\n中途的输出结果，目前是三十个txt"
    print "big_set_newnum:", big_set_newnum
    print "word_num:", word_num
    print "彭于晏的编号：", big_set_newnum["彭于晏"]  # 检查
    print "dictionary的数量：", len(dictionary_dy)
    print dictionary_dy
    # dictionary_dy.save('dictionary.dict')    # 不能这么写，因为这个dictionary不是corpora.Dictionary的对象

    # outi = 0 # 检查输出数目
    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if (OneFileName.find('.txt') == -1) or (root != dest):
                continue
            OneFullFileName = join(root, OneFileName)

            f = open(OneFullFileName)
            # l = f.read().decode('gb2312').encode('utf-8')  #这个在我的测试文件里面是正确的
            l = f.read().decode('gb2312', 'ignore').encode('utf-8')  # 这个在我的测试文件里面是正确的

            l = l[10:-1]  # 去除掉json中前后不需要的字符串
            dict_l = eval(l)
            list_txt = []

            # # 检查
            # list_txt.append((OneFileName, outi))  # 给每个文档列表头加入一个元组，（文件名，编号）
            # outi = outi + 1
            ########
            for word in dict_l:
                word_num = big_set_newnum[word]  # 在big_set_newnum里面这个词的编号
                tup = (word_num, dict_l[word])  # dict_l[word]代表在这篇文档中这个词出现的次数
                list_txt.append(tup)

            list_corpora.append(list_txt)

    # print "\n\n\n\n\n\n\n", "语料结果"
    # pprint(list_corpora)
'''





def data_preprocess(dest):
    """
    把dest文件夹中的所有 子文件夹中的 txt文件的数据读取并整理到一dictionary中
    :param dest: 文件夹地址
    :return:
    """
    num_window = 0
    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if OneFileName.find('.txt') == -1:
                continue
            OneFullFileName = join(root, OneFileName)

            f = open(OneFullFileName)
            # l = f.read().decode('gb2312').encode('utf-8')  #这个在我的测试文件里面是正确的
            # l = f.read().decode('gb2312', 'ignore').encode('utf-8')  # 忽略繁体字
            l = f.read().decode('utf-8', 'ignore').encode('utf-8')  # 忽略繁体字

            fill_Big_set(l)
            #
            # if OneFullFileName == 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata\TheTrumanShowTimeWindow\window\Window10.txt':
            #     fill_Big_set(l)

            num_window += 1



    print big_set

    word_num = -1
    for word in big_set:
        print word
        word_num += 1
        big_set[word] = word_num
        dictionary_dy.setdefault(word_num, word)  # 编号在前面

    # 做一次dictionary清理
    clean_dictionary(dictionary_dy)
    # 清理结束
    print "window.txt的个数：", num_window
    print "big_set:", big_set
    print "word_num:", word_num
    print "彭于晏的编号：", big_set["彭于晏"]  # 检查
    print "dictionary的数量：", len(dictionary_dy)
    print dictionary_dy
    file_dictionary()
    # dictionary_dy.save('dictionary.dict')    # 不能这么写，因为这个dictionary不是corpora.Dictionary的对象

    # fw 把list_corpora( [[],[],[],[],...] )写入文件
    fw = open(Global_projectDatapath + "\\list_corpus.txt", 'a')
    fw.truncate()
    Global_listcorpusCount = 0  # 写入list_corpus.txt加上当前文档的编号
    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if OneFileName.find('.txt') == -1:
                continue
            OneFullFileName = join(root, OneFileName)

            f = open(OneFullFileName)
            # l = f.read().decode('gb2312').encode('utf-8')  #这个在我的测试文件里面是正确的
            # l = f.read().decode('gb2312', 'ignore').encode('utf-8')  # 这个在我的测试文件里面是正确的
            l = f.read().decode('utf-8', 'ignore').encode('utf-8')  # 忽略繁体字
            f.close()

            fill_List_corpora(l, OneFullFileName, fw, Global_listcorpusCount)
            Global_listcorpusCount += 1

    fw.close()

    # print "\n\n\n\n\n\n\n", "语料结果"
    # pprint(list_corpora)

############################################################################################################

def clean_dictionary(dictobj):
    """
    对dictionary_dy做一个数据清洗，去除不需要的文字
    :param dictobj: dict对象
    :return: dictobj
    """
    clean_string = '你我他就是这些那些该走中文存在确认派子看字红笔toO'
    for key, value in dictobj.items():
        if str(value) in clean_string or str(key) in clean_string:
            del(dictobj[key])
    return dictobj



def file_dictionary():
    """
    打印dictionary到文件
    :return:
    """
    outfile = open(Global_projectDatapath + "\\dictionary_dy.txt", 'w')
    outfile.write("dictionary的数量： "+str(len(dictionary_dy)))
    outfile.write('\n\n\n')
    for key, value in dictionary_dy.items():
        outfile.write(str(key))
        outfile.write('\t')
        outfile.write(value)
        outfile.write('\n')
    outfile.close()



def fill_Big_set(l):
    """
    把一个window中的user的数据，依次读出，转化成字典，计入到big_set中

    :param l: 这里读入的l就是一整个window.txt 里的数据，是包括了{"id":112,"startTime":1120.0,"endTime":1150.0,"userAlive":25,
    "numOfDanmaku":26,"averageLength":6.076923076923077,"userFeature":   的用户评论数据

    :return: no return
    """

    userFeature_location = l.find('userFeature', 0)
    if userFeature_location == -1:
        return
    l = l[userFeature_location+13: -1]
    if len(l) == 0:
        return

    userDetail_location = l.find('detail', 0)
    while userDetail_location != -1:
        twobrace_location = l.find('}}', userDetail_location)
        userDetail = l[userDetail_location+8: twobrace_location+1]
        big_set.update(eval(userDetail))
        userDetail_location = l.find('detail', twobrace_location)






def fill_List_corpora(l, OneFullFileName, fw, listcorpuscount):
    """
    对list_corpora赋值  并把list_corpus内容写入fw中
    :param l: 一个window中的内容
    :param OneFullFileName: 当前写入的是哪个txt温江
    :return: no return
    """
    list_txt = []
    lcounter = Counter()   # 单独对每一个l（window中的内容）设置一个计数器
    userFeature_location = l.find('userFeature', 0)
    if userFeature_location == -1:
        return
    l = l[userFeature_location+13: -1]
    if len(l) == 0:
        return

    userDetail_location = l.find('detail', 0)
    while userDetail_location != -1:
        twobrace_location = l.find('}}', userDetail_location)
        userDetail = l[userDetail_location+8: twobrace_location+1]
        # big_set.update(eval(userDetail))

        lcounter.update(clean_dictionary(eval(userDetail)))  # 记录一个l（window）中的word和对应个数,并清理掉不需要的字段

        userDetail_location = l.find('detail', twobrace_location)

    for word in lcounter:
        word_num = big_set[word]
        tup = (word_num, lcounter[word])
        list_txt.append(tup)

    list_corpora.append(list_txt)
    fw.write('<'+str(listcorpuscount)+'>  '+OneFullFileName + '\n')
    listcorpuscount += 1
    fw.write(str(list_txt) + '\n\n')



if __name__ == "__main__":
    dest = "C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata"  # 需要input的地方！！！！！！！！

    data_preprocess(dest)


