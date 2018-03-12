#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docx import Document


def main():
    doc = Document(docx='疾病KG卡标准模板.docx')
    for para in doc.paragraphs:
        print(para.style.name, para.style.font.size, para.text)
        #for run in para.runs:
        #    print(run.style.type)


if __name__ == '__main__':
    main()
