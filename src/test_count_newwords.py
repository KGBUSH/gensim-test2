# encoding: utf-8
"""
计算一句话的主题分布
"""

from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint  # pretty-printer
from test_readTXTcontent import *

dest = "C:\Users\KGBUS\PycharmProjects\gensim-test\lzy_window_all"  # 需要改的地方！！！！！！！！

ldadest = 'corpus_dy_tfidf___dictionary_dy___10___1000.lda'  # 选择lda库

corpusmm = corpora.MmCorpus('corpus_dy_tfidf.mm')  # 读取语料库

oneuser_info = '"49b2bf00":{"detail":{"233":1,"无力":1,"吐槽":1,"这":1,"帮":1,"穿":1}}'

# data_preprocess函数的调用
data_preprocess(dest)


def oneuser_topics(user_words):
    """

    :param user_words：（str）形式为    {"233":1,"无力":1,"吐槽":1,"这":1,"帮":1,"穿":1}
    :return: 根据已有的语料库，字典，lda库。返回这句话的topics分布
             返回格式为：'{"0": 0.014290024382893432, "1": 0.014289438487241572}'
    """
    # userid = '11fd91a1'
    # user_words = {"就": 1, "什么": 1, "不错": 1, "流畅": 1, "看": 1, "画": 1, "完": 1, "能": 1, "原": 1}
    # userid = user_info[1:user_info.find('"', 1)]
    # user_words = eval(user_info[user_info.find('detail') + 8: -1])

    # # 输出dictionary_dy
    # for wordnum, word in dictionary_dy.items():
    #     print wordnum, ":", word,


    user_words = eval(user_words)
    new_user_words = {}  # 新的字典:user_words  -->  key用dictionary_dy里面的编号表示
    for (key, value) in user_words.items():
        for dickey, dicvalue in dictionary_dy.items():
            if key == dicvalue:
                new_user_words.update({dickey: value})

    # print "\n新的字典:user_words  -->  key用dictionary_dy里面的编号表示：", new_user_words
    words_list = []
    for (key, value) in new_user_words.items():
        words_list.append((key, value))

    lda = models.LdaModel.load(ldadest)  # 读入lda库

    newwords_lda = lda[words_list]  # 在原始语料库上加上双重包装: bow->tfidf->fold-in-lsi
    # print "\n\n"
    # i = 0
    # for doc in newwords_lda:
    #     print "第", i, "topic："
    #     i += 1
    #     print(doc)
    #
    # print newwords_lda
    # # print "转换成lzy的格式："
    user_str = "{"
    for tup in newwords_lda:
        topic = str(tup[0])
        weight = str(tup[1])
        user_str += '"' + topic + '"' + ':' + weight + ','
    user_str = user_str[:-1]
    user_str += '}'
    return user_str


def file_change(source, aim):
    """

    :param source: window文件名称，包含了userid，"7e56875a":{"detail":{"片":1,"安静":1,"看":1}}
    :param aim:  转换结果： "2d415ba6":{"detail":{"2":0.924997612819}}
    :return:  没有return
    """
    f = open(source, "r")
    str_file = f.read().decode('gb2312', 'ignore').encode('utf8')
    # print "打印文件内容：\n\n"
    # print str_file
    # print "\n\n"
    # 找出所有的需要改的：{"还有":1,"25":1,"今天":1,"小伙伴":1,"居然":1,"看":1,"一起":1}

    nowlocation = 0
    output_number = 0
    while nowlocation < len(str_file):
        detail_location = str_file.find('detail', nowlocation)
        if detail_location == -1:  # 到文件末尾了
            break
        nowlocation = detail_location
        twobracelocation = str_file.find('}}', nowlocation)

        now_user_words = str_file[detail_location + 8: twobracelocation + 1]
        topic_distribution = oneuser_topics(now_user_words)
        str_file = str_file.replace(now_user_words, topic_distribution)

        print output_number
        print now_user_words, "对应的分布：", topic_distribution
        nowlocation = str_file.find('}}', nowlocation)
        output_number += 1

    # print '要写入新文件的str：'
    # print str_file
    # print "改：\n\n\n"


    fp = open(aim, 'w')
    fp.write(str_file.decode('utf8').encode('gb2312', 'ignore'))
    fp.close()

    #
    # # 6d38b3fc
    # repla = '{"0":0.0142902420272,"1":0.0142896019395,"2":0.0142884148636,"3":0.0142867572929,' \
    #         '"4":0.376628090697,"5":0.0142887489596,"6":0.0142892312208,' \
    #         '"7":0.0142887906125,"8":0.509059049536,"9":0.0142910728517}'
    # fp.write(str_file.replace('{"导演":1,"相关":1,"强烈":1,"屏蔽":1,"弹幕":1,"字":1,"建议":1,"二":1,"不":1}', repla).decode('utf8').encode('gb2312','ignore'))

