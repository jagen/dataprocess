#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docx import Document


def main():
    doc = Document(docx='疾病KG卡标准模板.docx')
    file = open('output.md', 'w', encoding='utf-8')
    title = ''
    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            file.writelines('#' + para.text.replace(' (22个字)', '') + '\n')
            print(para.text, para.style.font.size.pt)
        elif para.style.name == 'Heading 2':
            file.writelines('##' + para.text.replace(' (22个字)', '') + '\n')
            print(para.text, para.style.font.size.pt)
        else:
            file.writelines(para.text + '\n')
            for run in para.runs:
                print(run.style.font.size)
    file.close()


if __name__ == '__main__':
    main()
