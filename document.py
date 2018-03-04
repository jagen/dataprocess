#!/usr/bin/env python
# -*- coding: utf-8 -*-
from docx2html import convert

def main():
    html = convert('滑膜炎.docx')
    print(html.encoding('utf-8'))

if __name__ == '__main__':
    main()