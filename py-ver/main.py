import re
import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("HAHA-Separator")
        
        # window size
        master.geometry("200x100")

        # label and input field
        self.label = tk.Label(master, text="Enter message:")
        self.label.pack()
        self.input = tk.Entry(master)
        self.input.pack()

        # button for conversion and bind it to function
        self.button1 = tk.Button(master, text="Convert HAHA", command=self.convert)
        self.button1.pack()

        # button for copying to clipboard and bind it to function
        self.button2 = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.button2.pack()
    
    # function to separate HAHA to HA HA
    def haha_separator(self):
        text = self.input.get()
        haha = re.split(r'(HA|ha|Ha|hA|HE|he|He|hE)', text)
        result =''.join(haha[x] if haha[x] != '' else ' ' for x in range(len(haha)))
        return result
    
    # function to show the converted data in an infobox
    def convert(self):
        result = self.haha_separator()
        if result != ' ':
            messagebox.showinfo("Converted Successfully", result)
        else:
            messagebox.showwarning("Error", "Please enter some text.")

    # function to copy converted data to the clipboard
    def copy_to_clipboard(self):
        result = self.haha_separator()
        if  result != ' ':
            self.master.clipboard_clear()
            self.master.clipboard_append(result)
            messagebox.showinfo("Converted and Copied", "Text successfully converted and copied to clipboard.")
        else:
            messagebox.showwarning("Error", "Please enter some text.")

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()