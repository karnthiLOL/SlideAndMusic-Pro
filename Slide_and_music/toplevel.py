import tkinter as tk


class SetTime(tk.Toplevel):
    def __init__(self,Frame):
        super().__init__()
        self.Frame = Frame
        self.width = 250
        self.height = 50
        self.geometry(
            "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2),
                                 self.winfo_screenheight() // 2 - (self.height // 2)))
        self.title('SetTime(Sec)')
        self.iconbitmap("./sys/icon.ico")
        self.entryTime = tk.StringVar()
        # self.entryTime.trace_add('write', self.entryTime)
        self.input = tk.Entry(self,textvariable= self.entryTime)
        self.input.pack()
        self.btn = tk.Button(self,text="submit" ,command = self.Submit)
        self.btn.pack()

    def Submit(self):
        print("data in self.entryTime variable" ,self.entryTime.get())
        self.Frame.setTime(self.entryTime.get())
        self.destroy()
        self.update()










