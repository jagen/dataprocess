#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import sys
import io

def main():
    jieba.load_userdict('userdict.txt')

    # 结巴分词--全模式
    SENT = '在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。'
    wordlist = jieba.cut(SENT, cut_all=True)
    print('|'.join(wordlist))

    # 结巴分词--精确切分
    wordlist = jieba.cut(SENT)
    print('|'.join(wordlist))

    # 结巴分词--搜索引擎模式
    wordlist = jieba.cut_for_search(SENT)
    print('|'.join(wordlist))

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
