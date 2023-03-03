#!/usr/bin/python
# -*-coding:UTF-8-*-

import os
from PyPDF3 import PdfFileReader, PdfFileMerger


def combine_pdf(files, out_path):
    merger = PdfFileMerger(strict=False)
    for f in files:
        file = PdfFileReader(open(f, 'rb'))
        if file.isEncrypted:
            file.decrypt('Aa3662090')  # 密碼請自行更改
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
                out_path=out_path)
    msg = 'OK'
else:
    msg = 'Matching multiple files'




from pdf2image import convert_from_path
pages = convert_from_path('C:/Users/wang/Desktop/11112_14660853_營業人銷售額與稅額申報書(401)_.pdf', dpi=200, first_page=1, last_page=1)
pages[0].save('example.jpg', 'JPEG')