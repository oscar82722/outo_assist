#!/usr/bin/python
# -*-coding:UTF-8-*-

import os
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter


def trans_encrypt_pdf(file_name):

    # convert pdf - png - pdf
    pages = convert_from_path(file_name, dpi=300)
    pages[0].save('./temp/temp.pdf')

    # resize page
    pdf_file = open('./temp/temp.pdf', 'rb')
    pdf_reader = PdfFileReader(pdf_file)
    pdf_writer = PdfFileWriter()

    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        page_w = float(page.mediaBox[2])
        page_h = float(page.mediaBox[3])

        if page_w > page_h:
            new_page_width = 842
            new_page_height = 595
            r = 842/page_w
        else:
            new_page_width = 595
            new_page_height = 842
            r = 595 / page_w

        new_page = pdf_writer.addBlankPage(
            new_page_width,
            new_page_height)

        new_page.mergeScaledTranslatedPage(
            page, r, 0, 0)

    with open('./temp/temp2.pdf', 'wb') as out:
        pdf_writer.write(out)

    pdf_file.close()


def combine_pdf(files, out_path):
    merger = PdfFileMerger(strict=False)
    for f in files:
        file_pdf = open(f, 'rb')
        file = PdfFileReader(file_pdf)
        if file.isEncrypted:
            file_pdf.close()
            trans_encrypt_pdf(f)
            file_pdf = open('./temp/temp2.pdf', 'rb')
            file = PdfFileReader(file_pdf)
        merger.append(file)
        file_pdf.close()

    merger.write(out_path)
    merger.close()


def run_combine_pdf(file_name,
                    target_folder,
                    out_folder,
                    code_index=0):
    # get company code
    file_code = \
        file_name.split('/')[-1].split('_')[code_index]

    # get data
    file_names = os.listdir(target_folder)
    target_file = [x for x in file_names if file_code in x]

    if len(target_file) == 0:
        msg = 'No matching files found'
    elif len(target_file) == 1:
        combine_pdf(
            files=[file_name,
                   target_folder + '/' + target_file[0]],
            out_path=out_folder + '/' + file_code + '.pdf')
        msg = 'OK'
    else:
        msg = 'Matching multiple files'

    return file_code + ' : ' + msg


if __name__ == '__main__':
    msg1 = run_combine_pdf(
        file_name='C:/Users/wang/Desktop/test data/請款單/14660123_立昇食品行_11201_請款明細表.pdf',
        target_folder='C:/Users/wang/Desktop/test data/401/',
        out_folder='C:/Users/wang/Desktop/test data/combine/',
        code_index=0
    )

    print(msg1)

