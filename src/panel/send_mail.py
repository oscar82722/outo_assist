#!/usr/bin/python
# -*-coding:UTF-8-*-

from tkinter import filedialog, ttk
import tkinter as tk
import time
import os


import src.sendemail as sm


class Sendmail:
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
                 "1. 附件檔名僅為統編。例 : 14660853.pdf",
            foreground="red", anchor="w")
        label1.pack(fill="x")

        # create folder 1
        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack(padx=10, pady=10)

        self.text1 = tk.Text(self.frame1, height=1)
        self.text1.pack(side=tk.LEFT)

        button1 = ttk.Button(self.frame1,
                             text="附件所在資料夾",
                             command=self.askdirectory1)
        button1.pack(side=tk.LEFT, padx=10)

        # create run button
        self.frame2 = ttk.Frame(self.root)
        self.frame2.pack(padx=10, pady=10)

        button4 = ttk.Button(
            self.frame2,
            text="執行   ",
            command=self.run_sent_mail)
        button4.pack(side=tk.RIGHT)

        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(padx=10, pady=10)
        self.text2 = tk.Text(self.frame3, height=30)
        self.text2.pack(side=tk.BOTTOM)

    def askdirectory1(self):
        # 開啟資料夾選擇對話框
        self.folder_path1 = filedialog.askdirectory()

        # 更新 Text 元件內容
        self.text1.delete('1.0', tk.END)  # 刪除原有內容
        self.text1.insert(tk.END, self.folder_path1)

    def run_sent_mail(self):
        # 更新 Text 元件內容
        self.text2.delete('1.0', tk.END)  # 刪除原有內容
        # check input file
        file_names = os.listdir(self.folder_path1)
        for f in file_names:
            msg = sm.run_sent(file=self.folder_path1+'/'+f)
            self.text2.insert(tk.END, msg + '\n')
            time.sleep(1)

        self.text2.insert(tk.END, '===== Done ===== \n')



