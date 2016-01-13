# encoding: utf-8


from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint  # pretty-printer
from test_readTXTcontent import *

print "开始"
print "这是一个测试读取txt的结果"
# data_preprocess()
print '\n'
print '\n'

documents = ["Human machine interface for lab abc computer computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

# 去除停用词并分词
# 译者注：这里只是例子，实际上还有其他停用词
# 处理中文时，请借助 Py结巴分词 https://github.com/fxsjy/jieba
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]
# 去除仅出现一次的单词

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]
print "每个文档中的tokens："
pprint(texts)

dictionary = corpora.Dictionary(texts)
print "直接输出dictionary："
print dictionary
dictionary.save('deerwester.dict')  # 把字典保存起来，方便以后使用

print "dictionary.token2id："
pprint(dictionary.token2id)

print "dictionary.id2token："
pprint(dictionary.id2token)
print "直接输出dictionary", st
print type(dictionary)

# test

for word in dictionary:
    print type(word), " ", type(dictionary[word])
    print word, " ", dictionary[word]

# 函数doc2bow()简单地对每个不同单词的出现次数进行了计数，并将单词转换为其编号，然后以稀疏向量的形式返回结果

corpus = [dictionary.doc2bow(text) for text in texts]  # doc2bow: 就是把一篇文档text转化成[(0, 1), (1, 3)]这样的形式
corpora.MmCorpus.serialize('deerwester.mm', corpus)  # 存入硬盘，以备后需
print "将记号化的文档转化成向量："
pprint(corpus)
print "非格式化的corpus"
print corpus

# 主题与转换

tfidf = models.TfidfModel(corpus)  # 第一步 -- 初始化一个模型
# 基于这个TF-IDF模型，我们可以将上述用词频表示文档向量表示为一个用tf-idf值表示的文档向量
corpus_tfidf = tfidf[corpus]

print "\n"
print "将上述用词频表示文档向量表示为一个用tf-idf值表示的文档向量：\n"
for doc in corpus_tfidf:
    print(doc)

# LSI
print "\n"
print "lsi跑出来的结果-语料可以选择原始词频统计 或者TF-IDF"
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)  # 初始化一个LSI转换
print lsi.print_topics(2)

corpus_lsi = lsi[corpus_tfidf]  # 在原始语料库上加上双重包装: bow->tfidf->fold-in-lsi

for doc in corpus_lsi:
    print(doc)










    #
    #
    #
    #
    #
    # # 主题与转换
    #
    # tfidf = models.TfidfModel(corpus_dy)  # 第一步 -- 初始化一个模型
    # # 基于这个TF-IDF模型，我们可以将上述用词频表示文档向量表示为一个用tf-idf值表示的文档向量
    # corpus_dy_tfidf = tfidf[corpus_dy]
    #
    #
    # print "\n"
    # print "将上述用词频表示文档向量表示为一个用tf-idf值表示的文档向量：\n"
    # for doc in corpus_tfidf:
    #     print(doc)
    #
    #
    # # LDA
    # print "\n"
    # print "lda跑出来的结果-语料可以选择原始词频统计 或者TF-IDF"
    # lda = models.LdaModel(corpus_dy_tfidf, id2word=dictionary, num_topics=10)
    # print lda.print_topics()  # 每次都不一样。
    # print lda.print_topic(0)
    #
    # corpus_lda = lda[corpus_dy_tfidf]  # 在原始语料库上加上双重包装: bow->tfidf->fold-in-lsi
    #
    # for doc in corpus_lda:
    #     print(doc)
