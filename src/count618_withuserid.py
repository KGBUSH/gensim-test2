# encoding: utf-8
"""
计算618个文件（包括了用户ID），并重新写入618个新文件
"""
import os
from os.path import join
from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint  # pretty-printer
from test_readTXTcontent import *
from test_count_newwords import *

source_adress = "C:\Users\KGBUS\PycharmProjects\window_lzy_618_userid"
aim_adress = "C:\Users\KGBUS\PycharmProjects\windows_topics_aim_1228_2225"


def process(sourcefolder, aimfolder):
    for root, dirs, files in os.walk(sourcefolder):
        for OneFileName in files:
            if (OneFileName.find('.txt') == -1) or (root != sourcefolder):
                continue
            inFullFileName = join(root, OneFileName)
            outFullFileName = join(aimfolder, OneFileName)

            print "\n\n\n\n\n", OneFileName
            file_change(inFullFileName, outFullFileName)







process(source_adress, aim_adress)