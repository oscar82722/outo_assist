#!/usr/bin/python
# -*-coding:UTF-8-*-

import tkinter as tk
from tkinter import ttk

import src.panel.combine_pdf as cb
import src.panel.send_mail as sm

if __name__ == '__main__':
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
    cb.CombinePdf(tab1)
    sm.Sendmail(tab2)
    root.mainloop()

