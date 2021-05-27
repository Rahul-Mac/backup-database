from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Backup Database")
        self.window.resizable(0,0)
        self.window.geometry("270x260")
        self.window.iconbitmap("icon.ico")
        self.widgets()
        self.window.mainloop()

    def widgets(self):
        self.frame = ttk.LabelFrame(self.window, text="Details")
        self.frame.grid(column = 0, row = 0, padx = 5, pady = 5)
        self.label = {}
        self.entry = {}
        self.fexpl = {}
        self.bttns = {}
        w = 20
        self.label["path"] = ttk.Label(self.frame, text = "MySQL Path")
        self.label["path"].grid(column = 0, row = 0, padx = 5, pady = 5)
        self.label["user"] = ttk.Label(self.frame, text = "MySQL Username")
        self.label["user"].grid(column = 0, row = 1, padx = 5, pady = 5)
        self.label["dbps"] = ttk.Label(self.frame, text = "Database Password")
        self.label["dbps"].grid(column = 0, row = 2, padx = 5, pady = 5)
        self.label["dbnm"] = ttk.Label(self.frame, text = "Database Name")
        self.label["dbnm"].grid(column = 0, row = 3, padx = 5, pady = 5)
        self.label["bpth"] = ttk.Label(self.frame, text = "Backup Path")
        self.label["bpth"].grid(column = 0, row = 4, padx = 5, pady = 5)
        self.label["bfnm"] = ttk.Label(self.frame, text = "Backup File Name")
        self.label["bfnm"].grid(column = 0, row = 5, padx = 5, pady = 5)

        self.bttns["path"] = ttk.Button(self.frame, width = w, text = "Choose Path", command = self.SelectPath)
        self.bttns["path"].grid(column = 1, row = 0, padx = 5, pady = 5)        
        self.entry["user"] = ttk.Entry(self.frame)
        self.entry["user"].grid(row = 1, column = 1, padx = 5, pady = 5)
        self.entry["dbps"] = ttk.Entry(self.frame)
        self.entry["dbps"].grid(row = 2, column = 1, padx = 5, pady = 5)
        self.entry["dbnm"] = ttk.Entry(self.frame)
        self.entry["dbnm"].grid(row = 3, column = 1, padx = 5, pady = 5)
        self.bttns["bpth"] = ttk.Button(self.frame, width = w, text = "Choose Path", command = self.ChoosePath)
        self.bttns["bpth"].grid(column = 1, row = 4, padx = 5, pady = 5)
        self.entry["bfnm"] = ttk.Entry(self.frame)
        self.entry["bfnm"].grid(row = 5, column = 1, padx = 5, pady = 5)
        self.bttns["conn"] = ttk.Button(self.frame, text = "Execute", command = self.DBConnect)
        self.bttns["conn"].grid(column = 0, row = 6, padx = 5, pady = 5)
        self.bttns["cler"] = ttk.Button(self.frame, text = "Reset", command = self.Reset)
        self.bttns["cler"].grid(column = 1, row = 6, padx = 5, pady = 5)
        
    def ChoosePath(self):
        self.path = filedialog.askdirectory()
        self.bttns["bpth"]["text"] = self.path

    def SelectPath(self):
        self.p = filedialog.askdirectory()
        self.bttns["path"]["text"] = self.p

    def message(self):
        messagebox.showinfo("Message", "Success! Check your backup file.")
  
    def error(self):
        messagebox.showerror("Message", "Error! Please enter the data correctly.")

    def DBConnect(self):
        try:
            if(self.entry["bfnm"].get() == "" or self.path == "" or self.entry["user"].get() == "" or self.entry["dbps"].get() == "" or self.entry["dbnm"].get() == ""):
                raise Exception()            
            u = self.entry["user"].get()
            p = self.entry["dbps"].get()
            d = self.entry["dbnm"].get()
            f = self.entry["bfnm"].get()
            h = "localhost"
            x = ""
            for i in f:
                if(i == "."):
                    break
                x += i
            os.popen(self.p[0]+": & cd "+self.p+" & "+"mysqldump.exe -e -h "+h+" -u "+u+" --password="+p+" "+d+" > "+self.path+"/"+x+".sql 2>&1")
            self.message()
        except:
            self.error()

    def Reset(self):
        self.bttns["bpth"]["text"] = "Choose Path"
        self.path = ""
        self.bttns["path"]["text"] = "Choose Path"
        self.p = ""
        self.entry["user"].delete(0,END)
        self.entry["dbps"].delete(0,END)
        self.entry["dbnm"].delete(0,END)
        self.entry["bfnm"].delete(0,END)
        
if __name__ == "__main__":
    Window()
