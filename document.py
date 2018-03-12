#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import sys
import io


def main():
    xml = etree.parse('滑膜炎/word/document.xml')
    root = xml.getroot()
    ns = root.nsmap
    body = xml.xpath('//w:document/w:body', namespaces=ns)
    print(body)
    textList = body[0].xpath('//w:p[1]/w:r/w:t', namespaces=ns)
    for t in textList:
        print(t.text)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
