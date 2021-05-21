import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def help_button():
    help_button = Tk()
    help_button.geometry('300x130+600+300')
    help_button.title('Help')
    help_label = Label(help_button, text='Made by THE-CEO-OF-MILK', bg='red')
    help_label2 = Label(help_button, text='Ctrl+A = select all')
    help_label3 = Label(help_button, text='Ctrl+C = copy')
    help_label4 = Label(help_button, text='Ctrl+X = cut')
    help_label5 = Label(help_button, text='Ctrl+V = paste')
    help_label.pack()
    help_label2.pack()
    help_label3.pack()
    help_label4.pack()
    help_label5.pack()
    help_button.mainloop

window = tk.Tk()
window.title("Text Editor By THE-CEO-OF-MILK")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As", command=save_file)
btn_help = tk.Button(fr_buttons, text="Help", command=help_button)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_help.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

print('hello there feel free to see the code and edit whatever you want here, the consloe is useless here...')

window.mainloop()
