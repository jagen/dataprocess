#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors
import time, timeit
import sys
import io
import pdb

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdb.set_trace()
t0 = time.clock()
#wv_from_text = KeyedVectors.load_word2vec_format('/Users/jagenzhao/dataprocess/word2vec/Tencent_AILab_ChineseEmbedding.txt')
#wv_from_text.init_sims(replace=True)
#wv_from_text.save('/Users/Jagen/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.models')
model = KeyedVectors.load('/Users/jagenzhao/dataprocess/word2vec/Tencent_AILab_ChineseEmbedding.models', mmap = 'r')
print('load models ok.', time.clock() - t0, 's\n')

t0 = time.clock()
print(u'白发')
keys = model.similar_by_word('白发', topn=100)
for key in keys:
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('斑丘疹')
for key in model.similar_by_word('斑丘疹', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('背痛')
for key in model.similar_by_word('背痛', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('糖尿病')
for key in model.similar_by_word('糖尿病', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('癫痫')
for key in model.similar_by_word('癫痫', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('羊角风')
for key in model.similar_by_word('羊角风', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('淋巴肉芽肿')
for key in model.similar_by_word('淋巴肉芽肿', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

t0 = time.clock()
print('\n')
print('白带带血')
for key in model.similar_by_word('白带带血', topn=100):
    print(key)
print('cost %f' %(time.clock() - t0))

while True:
    str = input(u'请输入：')
    if str == 'q' or str == 'Q':
        exit(0)

    for key in model.similar_by_word(str, topn=100):
        print(key)