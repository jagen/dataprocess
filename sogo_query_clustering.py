#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyltp import Segmentor
import codecs
import sys
import os

LTP_DATA_DIR = '/usr/local/ltp_data'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
segmentor = Segmentor()
segmentor.load(cws_model_path)

def processLine(line: str, no: int):
    # 获得分词
    words = segmentor.segment(line)
    print(str(no) + '\t' + '\t'.join(words))

def main():
    fd = codecs.open('痔疮相关热搜词（搜狗）.txt', 'r', 'utf-8')
    line = fd.readline()
    i = 1
    while line:
        processLine(line.split()[0], i)
        line = fd.readline()
        i = i + 1
    fd.close()

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
    