import tkinter as tk

def new_map(root):
    New_map = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
    New_map.pack_forget()

    label = tk.Label(New_map, text="Hello World")
    label.pack()

    return(New_map)

def new_map_affichage(New_map: tk.Frame):
    New_map.pack()