# encoding: utf-8

import os
from os.path import join
from collections import Counter


def main():
    dest = "C:\Users\KGBUS\PycharmProjects\gensim-test"
    outfile = open("output.txt", "w")
    arr = []
    for root, dirs, files in os.walk(dest):
        for OneFileName in files:
            if OneFileName.find('.txt') == -1:
                continue
            OneFullFileName = join(root, OneFileName)
            print root, " ", dirs, " ", files
            # for line in open(OneFullFileName, 'r'):
            #     print line

            f = open(OneFullFileName, 'r')
            for line in f.readlines():
                print line


# def function1():
#     c = Counter()

# if __name__ == "__main__":
#     # main()

print "一些输出："
c = Counter("asdfsaas")
print "第34行输出：", c['a']

c = Counter({'a': 2, 'c': 2, 'd': 1, 'b': 0})
del c['a']
print "第38行输出：", c

name_a = "2333"
count_a = 2
dict1 = {'Name': -1, 'Age': 7}
dict2 = {name_a: count_a}
dict3 = {'Name': 3, "apple": 8}

dict1.update(dict2)
print "Value : %s" % dict1

d = Counter()
d.update(dict1)
d.update(dict2)
d.update(dict3)
print "第53行输出：", d


print "更改Counter"
i = 0
for word in d:
    d[word] = i
    i = i + 1
print "第61行：", d
list_corpora = []
list_txt1 = []
for word in dict1:
    word_num = d[word]
    tup = (word_num, dict1[word])
    list_txt1.append(tup)
print dict1
print list_txt1
list_corpora.append(list_txt1)
list_corpora.append([(2, 5), (5, 8)])
print list_corpora


print '\xe6\x98\xaf'
print '\xe5\xa5\xbd'


print "\n\n"
name_a = "Name3"
count_a = 2
dict1 = {'Name': 4, 'Age': 7}
dict2 = {name_a: count_a}

dict1.update(dict2)
dict1.setdefault('kk', 3)
print dict1
print len(dict1)


print "\xe6\x94\xbe\xe6\x98\xa0\xe5\xae\xa4"
