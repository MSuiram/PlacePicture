import tkinter as tk

def open_map(root):
    Open_map = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
    Open_map.pack_forget()

    label = tk.Label(Open_map, text="Open Map")
    label.pack()

    return(Open_map)

def open_map_affichage(Open_map: tk.Frame):
    Open_map.pack()