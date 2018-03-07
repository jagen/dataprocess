#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyltp import SentenceSplitter
from pyltp import Segmentor
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 分词
LTP_DATA_DIR = '/Users/Jagen/ltp_data/'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
segmentor = Segmentor()
segmentor.load(cws_model_path)
words = segmentor.segment('元芳你怎么看')
print('\t'.join(words))
segmentor.release()

# 使用外部词典
segmentor = Segmentor()
segmentor.load_with_lexicon(cws_model_path, './lexicon')
#segmentor.load(cws_model_path)
words = segmentor.segment('亚硝酸盐是一种化学物质')
print('\t'.join(words))
segmentor.release()

# 分句
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')
print("\n".join(sents))

# 词性标注
from pyltp import Postagger
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
postagger = Postagger()
postagger.load(pos_model_path)

words = ['元芳', '你', '怎么', '看']
postags = postagger.postag(words)

print('\t'.join(postags))
postagger.release()
