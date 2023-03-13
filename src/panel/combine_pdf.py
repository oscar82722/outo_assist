#!/usr/bin/python
# -*-coding:UTF-8-*-

from tkinter import filedialog, ttk
import tkinter as tk
import os

import src.util as ut


class CombinePdf:
    def __init__(self, root):
        # save folder path
        self.root = root
        self.folder_path1 = None
        self.folder_path2 = None
        self.folder_path3 = None

        # create note
        self.frame0 = ttk.Frame(self.root)
        self.frame0.pack(padx=10, pady=10)
        label1 = tk.Label(
            self.frame0,
            text="本程式以 '統編' 作為配對方式，因此 \n"
                 "1. 401 檔名中必需以 '_' 作為連接符號，統編需為第2個位置"
                 "例 : 11112_14660852_營業人銷售額與稅額申報書(401)_.pdf \n"
                 "2. 請款單檔名必須要有 統編",
            foreground="red", anchor="w")
        label1.pack(fill="x")

        # create folder 1
        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack(padx=10, pady=10)

        self.text1 = tk.Text(self.frame1, height=1)
        self.text1.pack(side=tk.LEFT)

        button1 = ttk.Button(self.frame1,
                             text="401檔案 資料夾",
                             command=self.askdirectory1)
        button1.pack(side=tk.LEFT, padx=10)

        # create folder 2
        self.frame2 = ttk.Frame(self.root)
        self.frame2.pack(padx=10, pady=10)

        self.text2 = tk.Text(self.frame2, height=1)
        self.text2.pack(side=tk.LEFT)

        button2 = ttk.Button(
            self.frame2,
            text="請款單 資料夾  ",
            command=self.askdirectory2)
        button2.pack(side=tk.LEFT, padx=10)

        # create folder 3
        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(padx=10, pady=10)

        self.text3 = tk.Text(self.frame3, height=1)
        self.text3.pack(side=tk.LEFT)

        button3 = ttk.Button(
            self.frame3,
            text="檔案輸出位置   ",
            command=self.askdirectory3)
        button3.pack(side=tk.LEFT, padx=10)

        # create run button
        self.frame4 = ttk.Frame(self.root)
        self.frame4.pack(padx=10, pady=10)

        button4 = ttk.Button(
            self.frame4,
            text="執行   ",
            command=self.run_combine)
        button4.pack(side=tk.RIGHT)

        self.frame5 = ttk.Frame(self.root)
        self.frame5.pack(padx=10, pady=10)
        self.text4 = tk.Text(self.frame5, height=30)
        self.text4.pack(side=tk.BOTTOM)

    def askdirectory1(self):
        # 開啟資料夾選擇對話框
        self.folder_path1 = filedialog.askdirectory()

        # 更新 Text 元件內容
        self.text1.delete('1.0', tk.END)  # 刪除原有內容
        self.text1.insert(tk.END, self.folder_path1)

    def askdirectory2(self):
        # 開啟資料夾選擇對話框
        self.folder_path2 = filedialog.askdirectory()

        # 更新 Text 元件內容
        self.text2.delete('1.0', tk.END)  # 刪除原有內容
        self.text2.insert(tk.END, self.folder_path2)

    def askdirectory3(self):
        # 開啟資料夾選擇對話框
        self.folder_path3 = filedialog.askdirectory()

        # 更新 Text 元件內容
        self.text3.delete('1.0', tk.END)  # 刪除原有內容
        self.text3.insert(tk.END, self.folder_path3)

    def run_combine(self):
        # 更新 Text 元件內容
        self.text4.delete('1.0', tk.END)  # 刪除原有內容
        # check input file
        file_names = os.listdir(self.folder_path1)
        for f in file_names:
            msg = ut.run_combine_pdf(
                file_name=self.folder_path1+'/'+f,
                target_folder=self.folder_path2,
                out_folder=self.folder_path3
            )
            self.text4.insert(tk.END, msg + '\n')
            self.text4.update_idletasks()
        self.text4.insert(tk.END, '===== Done ===== \n')
