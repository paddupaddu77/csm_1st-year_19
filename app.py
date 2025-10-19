import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

# Create main window
root = tk.Tk()
root.title("Notepad Clone")
root.geometry("800x600")

# Text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

# File operations
current_file = None

def new_file():
    global current_file
    if text_area.edit_modified():
        if messagebox.askyesno("Unsaved Changes", "Do you want to save changes?"):
            save_file()
    text_area.delete(1.0, tk.END)
    current_file = None
    root.title("Notepad Clone - New File")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        current_file = file_path
        root.title(f"Notepad Clone - {file_path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Saved", "File saved successfully.")
    else:
        save_as()

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        current_file = file_path
        root.title(f"Notepad Clone - {file_path}")
        messagebox.showinfo("Saved", "File saved successfully.")

def exit_app():
    if text_area.edit_modified():
        if messagebox.askyesno("Unsaved Changes", "Do you want to save before exiting?"):
            save_file()
    root.destroy()

# Menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Start the application
root.mainloop()
