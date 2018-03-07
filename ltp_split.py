#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
import sys, io

def split_word():
    mode_path = '/Users/Jagen/ltp_data/cws.model'
    segmentor = Segmentor()
    segmentor.load(mode_path)
    sent = '在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。'
    words = segmentor.segment(sent)
    print('|'.join(words))

def pos_word():
    mode_path = '/Users/Jagen/ltp_data/pos.model'
    send = '在 包含 问题 的 所有 解 的 解空间树 中 ， 按照 深度优先 搜索 的 策略 ， 从 根节点 出发 深度 探索 解空间树 。'
    words = send.split(' ')
    postagger = Postagger()
    postagger.load(mode_path)
    postags = postagger.postag(words)
    for word, postag in zip(words, postags):
        print(word + "/" + postag,)

def ner_word():
    mode_path = '/Users/Jagen/ltp_data/ner.model'


def main():
    split_word()
    pos_word()

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
