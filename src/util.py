#!/usr/bin/python
# -*-coding:UTF-8-*-

import os
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter


def read_encrypt_pdf(file_name):
    pages = convert_from_path(file_name, dpi=300)
    pages[0].resize((842, 595))
    pages[0].save('./temp/temp.pdf')

    pdf_reader = PdfFileReader(open('./temp/temp.pdf', 'rb'))
    # 設置頁面大小為 A4
    # 創建 PDF 寫入器
    pdf_writer = PdfFileWriter()

    # 遍歷每個頁面
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        # 計算新的頁面大小
        new_page_width = 842
        new_page_height = 595

        # 創建新的頁面對象
        new_page = pdf_writer.addBlankPage(new_page_width,
                                           new_page_height)

        # 縮放頁面並寫入到新的頁面對象中
        new_page.mergeScaledTranslatedPage(page, 0.24, 0,
                                           0)

    # 將調整後的PDF寫入新的檔案
    with open('./temp/temp2.pdf', 'wb') as out:
        pdf_writer.write(out)

    file = PdfFileReader(open('./temp/temp2.pdf', 'rb'))
    return file


def combine_pdf(files, out_path):
    merger = PdfFileMerger(strict=False)
    for f in files:
        file = PdfFileReader(open(f, 'rb'))

        if file.isEncrypted:
            file = read_encrypt_pdf(f)

        merger.append(file)
    merger.write(out_path)
    merger.close()


file_name = 'C:/Users/wang/Desktop/新增資料夾/1/11112_14660853_營業人銷售額與稅額申報書(401)_.pdf'
target_folder = 'C:/Users/wang/Desktop/新增資料夾/2/'
out_path = 'C:/Users/wang/Desktop/新增資料夾/3/'

# get company code
file_code = file_name.split('/')[-1].split('_')[1]

# get data
file_names = os.listdir(target_folder)
target_file = [x for x in file_names if file_code in x]

if len(target_file) == 0:
    msg = 'No matching files found'
elif len(target_file) == 1:
    combine_pdf(files=[file_name,
                       target_folder+target_file[0]],
                out_path=out_path+file_code+'.pdf')
    msg = 'OK'
else:
    msg = 'Matching multiple files'
