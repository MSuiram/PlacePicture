import tkinter as tk
from main import creat_folium

def get_entry_value(entree: tk.Entry):
    return entree.get()

def creat_new_map(entree_name, entree_path):
    name = get_entry_value(entree_name)
    path = get_entry_value(entree_path)
    creat_folium(name, path)

def new_map(root):
    New_map = tk.Frame(root, borderwidth=2)
    New_map.pack_forget()

    title = tk.Label(New_map, text="Creat New Map", font=("Arial", 16, "bold"))
    title.pack()

    map_name_label = tk.Label(New_map, text="Name of New Map :")
    map_name_label.pack()

    map_name_entree = tk.Entry(New_map, textvariable=str, width=30)
    map_name_entree.pack()

    path_label = tk.Label(New_map, text="Path :")
    path_label.pack()

    path_entree = tk.Entry(New_map, textvariable=str, width=30)
    path_entree.pack()

    entry_button = tk.Button(New_map, text="Entry", command=lambda: creat_new_map(map_name_entree, path_entree))
    entry_button.pack()

    return(New_map)