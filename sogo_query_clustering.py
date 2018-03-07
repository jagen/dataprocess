#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys
import io
import os


def main():
    fd = codecs.open('痔疮相关热搜词（搜狗）.txt', 'r', 'utf-8')
    line = fd.readline()
    i = 1
    while line:
        line = fd.readline()
        i = i + 1
    fd.close()

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
    