#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#wv_from_text = KeyedVectors.load_word2vec_format('/Users/Jagen/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.txt')
#wv_from_text.init_sims(replace=True)
#wv_from_text.save('/Users/Jagen/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.models')
model = KeyedVectors.load('/Users/Jagen/Downloads/Tencent_AILab_ChineseEmbedding/Tencent_AILab_ChineseEmbedding.models', mmap = 'r')
print('load models ok.')
print(u'人民')
for key in model.similar_by_word(u'人民', topn=100):
    print(key)

print('\n')
print('甲流')
for key in model.similar_by_word(u'甲流', topn=100):
    print(key)

print('\n')
print('折返现象')
for key in model.similar_by_word(u'折返现象', topn=100):
    print(key)

print('\n')
print('糖尿病')
for key in model.similar_by_word(u'糖尿病', topn=100):
    print(key)

print('\n')
print('癫痫')
for key in model.similar_by_word(u'癫痫', topn=100):
    print(key)


print('\n')
print('羊角风')
for key in model.similar_by_word(u'羊角风', topn=100):
    print(key)

print('\n')
print('梦游')
for key in model.similar_by_word(u'梦游', topn=100):
    print(key)