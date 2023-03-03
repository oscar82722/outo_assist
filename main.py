#!/usr/bin/python
# -*-coding:UTF-8-*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# main
root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)
# panel for data combine
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='檔案合併')
# panel for sent mail
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='寄信')
tabControl.pack(expand=1, fill="both")


class MyApp:
    def __init__(self, root):
        self.root = root
        self.folder_path1 = None
        self.folder_path2 = None
        self.folder_path3 = None

        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack(padx=10, pady=10)

        self.text1 = tk.Text(self.frame1, height=1)
        self.text1.pack(side=tk.LEFT)

        button1 = ttk.Button(self.frame1, text="401檔案 資料夾", command=self.askdirectory1)
        button1.pack(side=tk.LEFT, padx=10)

        self.frame2 = ttk.Frame(self.root)
        self.frame2.pack(padx=10, pady=10)

        self.text2 = tk.Text(self.frame2, height=1)
        self.text2.pack(side=tk.LEFT)

        button2 = ttk.Button(self.frame2, text="請款單 資料夾  ", command=self.askdirectory2)
        button2.pack(side=tk.LEFT, padx=10)

        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(padx=10, pady=10)

        self.text3 = tk.Text(self.frame3, height=1)
        self.text3.pack(side=tk.LEFT)

        button3 = ttk.Button(self.frame3, text="檔案輸出位置   ", command=self.askdirectory3)
        button3.pack(side=tk.LEFT, padx=10)

        self.frame4 = ttk.Frame(self.root)
        self.frame4.pack(padx=10, pady=10)

        button4 = ttk.Button(self.frame4, text="執行   ", command='')
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


app = MyApp(tab1)
root.mainloop()
