#!/usr/bin/python
# -*-coding:UTF-8-*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='檔案合併')
tabControl.add(tab2, text='寄信')
tabControl.pack(expand=1, fill="both")


# 選擇資料夾
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# 設置按鈕
select_button = tk.Button(root, text="選擇資料夾", command=select_folder)
select_button.pack(pady=10)




ttk.Label(tab1,
          text="Welcome to \
          GeeksForGeeks").grid(column=0,
                               row=0,
                               padx=30,
                               pady=30)
ttk.Label(tab2,
          text="Lets dive into the\
          world of computers").grid(column=0,
                                    row=0,
                                    padx=30,
                                    pady=30)

root.mainloop()
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("回傳值的介面")

        self.label = tk.Label(master, text="請輸入數字：")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="確定", command=self.return_value)
        self.button.pack()

    def return_value(self):
        input_value = self.entry.get()
        self.master.destroy()
        return input_value

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print(app.return_value())