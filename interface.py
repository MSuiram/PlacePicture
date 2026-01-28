import tkinter as tk
from ui_new_map import new_map
from ui_open_map import *

def interface_display(interfaces: dict[str, tk.Frame], to_display):
    for name, interface in interfaces.items():
        if name == to_display:
            interface.pack(fill='both', expand=True)
        else:
            interface.pack_forget()

root = tk.Tk()
root.geometry('400x300')  

menubar = tk.Menu(root)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="New Map", command=lambda: interface_display(interfaces, "new_map_interface"))
menu1.add_command(label="Open Map", command=lambda: interface_display(interfaces, "open_map_interface"))
menubar.add_cascade(label="Files", menu=menu1)

root.config(menu=menubar)

interfaces = {"new_map_interface": new_map(root),"open_map_interface": open_map(root)}



root.mainloop()