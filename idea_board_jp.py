# coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg
import random

# ボタンがクリックされたときの処理
def ButtonClick():
    tmsg.showinfo("ヘルプ", "一時的にドキュメントを保存するアプリです。終了すると同時に保存してあるドキュメントは削除されるのでご注意ください。　　　　")

# メインのプログラム
root = tk.Tk()
root.geometry("650x565")
root.title("アイディアボード Ver.0.1.2")

# 履歴表示のテキストボックスを作る
rirekibox = tk.Text(root, font=("Helvetica", 10))
rirekibox.place(x=10, y=0, width=630, height=500)


button1 = tk.Button(root, text = "ヘルプ", font=("Helvetica", 10), command=ButtonClick)
button1.place(x = 590, y = 530)

root.mainloop()
