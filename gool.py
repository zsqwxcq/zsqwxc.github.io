import tkinter as tk
import os

def open_file():
    os.startfile("C:\\Users\\Ярослав\\3D Objects\\doppw.docx")

root = tk.Tk()

button = tk.Button(root, text="Открыть игру", command=open_file)
button.pack()

root.mainloop()