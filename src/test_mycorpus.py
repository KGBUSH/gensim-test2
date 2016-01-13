# encoding: utf-8
"""
训练模型
"""

from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint  # pretty-printer
from test_readTXTcontent import *
from globalValue import *
import globalValue





# 训练语料库的电影存放文件夹
dest = 'C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata'  # 需要input的地方！！！！！！！！





num_topics_LdaModel = 20    # LdaModel中的两个参数设置
iterations_LdaModel = 1000
dictionary_LdaModel = '3dic'

# LDA库的名称
ldasave_lda = "corpus_dy_tfidf___dictionary_dy___" \
              + str(num_topics_LdaModel) + "___" \
              + str(iterations_LdaModel) + "___"\
              + dictionary_LdaModel\
              + ".lda"
# ldasave_lda = 'corpus_dy_tfidf___dictionary_dy___20___1000.lda'  # LDA训练模型保存
corpussave_mm = 'corpus_dy_tfidf.mm'

# topicssave_txt = "txtall_t20_it1000.txt"
topicssave_txt = "txtall_t" + str(num_topics_LdaModel)\
                 + "_it" + str(iterations_LdaModel) \
                 + "_" +dictionary_LdaModel + ".txt"



data_preprocess(dest)

# 这里可以加一个处理：去除仅出现一次的单词



def do_LDA():

    print '\n'
    print '\n'

    # 主题与转换
    tfidf = models.TfidfModel(list_corpora)  # 第一步 -- 初始化一个模型
    # 基于这个TF-IDF模型，我们可以将上述用词频表示文档向量表示为一个用tf-idf值表示的文档向量
    corpus_dy_tfidf = tfidf[list_corpora]

    corpora.MmCorpus.serialize(Global_projectDatapath+'\\'+corpussave_mm, corpus_dy_tfidf)  # 把该语料库存下来，这个语料库只和输入的文件有关。和LDA无关

    # print "\n"
    # print "将上述用词频表示文档向量表示为一个用tf-idf值表示的文档向量：\n"
    # for doc in corpus_dy_tfidf:
    #     print(doc)

    # LDA
    print "\n"
    print "lda跑出来的结果-语料可以选择原始词频统计 或者TF-IDF"
    lda = models.LdaModel(corpus_dy_tfidf, id2word=dictionary_dy, num_topics=num_topics_LdaModel,
                          iterations=iterations_LdaModel)  # !!!!!!!!!!!!!!!!!!!!!!!注意topic的数目

    lda.save(Global_projectDatapath + '\\' + ldasave_lda)

    print str(lda.print_topics()).decode('utf-8', 'ignore').encode('utf-8')  # 每次都不一样。
    # def print_topics(self, num_topics=10, num_words=10): 默认只输出10*10

    print "一个一个输出："
    for i in xrange(num_topics_LdaModel):
        print lda.print_topic(i)

    topicinfo_to_mytxt(num_topics_LdaModel, lda)  # 把训练出来的topic输出到文件  # 需要input的地方！！！！！！！！

    corpus_lda = lda[corpus_dy_tfidf]  # 在原始语料库上加上双重包装: bow->tfidf->fold-in-lsi

    # 输出dictionary_dy
    print "\n\n"
    for wordnum, word in dictionary_dy.items():
        print wordnum, ":", word,
    print "\n\n"

    # 把corpus_lda写入文件中
    corpustopics_to_mytxt(corpus_lda)

    # 打印相似度
    print "\n\n相似度打印"
    document_similarity()










###############################################################################################

# 把主题详情 输入到文本中
def topicinfo_to_mytxt(num_topics, lda):
    """
    # 把主题详情 输入到文本中
    :param num_topics: num_topics_LdaModel = 20    # LdaModel中的两个参数设置
    :param lda: lda库
    :return:
    """
    f = open(Global_projectDatapath + '\\' + topicssave_txt, 'w')

    for i in xrange(num_topics):
        f.write("第" + str(i) + "个topic:\n")
        f.write(lda.print_topic(i))

        f.write("\n\n")

    f.close()






def corpustopics_to_mytxt(corpus_lda):
    """
    # 把corpus_lda写入文件中
    :param corpus_lda:  corpus_lda = lda[corpus_dy_tfidf]  # 得出了主题分布
    :return:
    """
    fw = open(Global_projectDatapath + "\\corpus_themeDistribution.txt", 'a')
    fw.truncate()
    docnum = 0
    for doc in corpus_lda:
        docid = "第" +str(docnum) + "篇："
        print docid
        fw.write(docid + '\n')
        docnum += 1
        print(doc)
        fw.write(str(doc) + '\n\n')
    fw.close()





def document_similarity():
    # dictionary = corpora.Dictionary.load('dictionary.dict')

    corpus = corpora.MmCorpus(Global_projectDatapath + '\\' + corpussave_mm)
    lda = models.LdaModel.load(Global_projectDatapath + '\\' + ldasave_lda)  # result from running online lda (training)

    index = similarities.MatrixSimilarity(lda[corpus])

    # 打印index到console
    print "\n\n打印index到console"
    for tup in index:
        print str(tup)

    index.save(Global_projectDatapath + '\\' + "simIndex.txt")  # index所对应的的就是list_corpora中的文档顺序

    # docname = "docs/the_doc.txt"
    # doc = open(docname, 'r').read()
    # vec_bow = dictionary_dy.doc2bow(doc.lower().split())

    # C:\Users\KGBUS\PycharmProjects\gensim-test2\lzy_severalMovieDanmudata\ShawshankTimeWindow\window\Window589.txt
    vec_bow = [(263, 1), (4399, 1), (12250, 1), (11635, 2), (11991, 4), (15614, 2), (9944, 1), (11469, 4),
               (3348, 4), (4148, 14), (7275, 1), (16171, 2), (13065, 1), (3371, 1), (8682, 1), (6979, 1),
               (8145, 2), (15370, 2), (5843, 1), (10992, 2), (13598, 1), (9478, 1), (7639, 1), (14389, 1),
               (14661, 1), (13260, 3), (6060, 1), (7119, 1), (15164, 1), (5809, 1), (1080, 1), (8978, 2),
               (4464, 1), (2093, 1), (11515, 2), (5013, 1), (5014, 4), (6078, 2), (13885, 1), (6879, 1),
               (11525, 1), (2106, 1), (14930, 2), (14931, 1), (10329, 1), (13365, 1), (13366, 1), (8998, 12),
               (14565, 2), (12864, 1), (9006, 1), (14108, 2), (14170, 1), (13382, 2), (6905, 1), (16250, 4),
               (5047, 1), (2905, 1), (10534, 1), (13392, 1), (12343, 1), (15737, 1), (6648, 1), (8225, 1),
               (932, 1), (868, 2), (14458, 2), (8496, 1), (972, 1), (366, 1), (15476, 2), (9294, 3), (682, 2),
               (11332, 2), (13858, 2), (13323, 1), (1162, 1), (7720, 1), (6691, 1), (2951, 1), (13438, 1),
               (1177, 1), (4542, 13), (13272, 2), (4841, 1), (2701, 2), (3783, 1), (16604, 4), (12675, 1),
               (2199, 2), (4591, 2), (11369, 6), (8551, 2), (4594, 1), (12959, 4), (13744, 1), (11645, 1),
               (8556, 1), (4732, 1), (14848, 1), (190, 1), (13227, 4), (4613, 1), (9883, 1), (15775, 1), (12707, 1),
               (7783, 1), (2239, 1), (12714, 1), (8592, 3), (2319, 1), (13496, 1), (6764, 1), (6236, 1), (14295, 1),
               (3294, 3), (14302, 3), (5994, 1), (8085, 1), (10311, 1), (9921, 1), (2782, 1), (3938, 1), (9149, 1),
               (16658, 1), (7323, 1), (6270, 1), (7764, 1), (13280, 3), (4115, 1), (10179, 1), (15364, 1), (491, 1),
               (9936, 1), (8897, 1), (9682, 1), (11045, 1)]

    vec_lda = lda[vec_bow]

    sims = index[vec_lda]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print sims

    fsims = open(Global_projectDatapath + '\\' + 'sims_now.txt', 'w')  # 把当前的相似度列表
    simnum = 0
    for tup in sims:
        fsims.write(str(tup) + '\n')
        simnum += 1
        if simnum == 20:
            break
    fsims.close()











if __name__ == "__main__":
    do_LDA()

