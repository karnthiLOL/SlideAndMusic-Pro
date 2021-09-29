from os import listdir
from os.path import isfile, join
import threading
import ctypes
import time
import tkinter as tk
from PIL import Image
class FrameSlid(tk.Toplevel):
    def __init__(self,Frame):
        super().__init__()
        self.Frame = Frame
        # self.width = 1280
        # self.height = 720
        # self.geometry(
        #     "{}x{}+{}+{}".format(self.width, self.height, self.winfo_screenwidth() // 2 - (self.width // 2),
        #                          self.winfo_screenheight() // 2 - (self.height // 2)))
        self.title('Play')
        self.iconbitmap("./sys/icon.ico")

        # Frame2
        self.frameBtn = tk.Frame(self)
        self.btn = tk.Button(self.frameBtn, text="Stop", font=(16), command=self.Stop)
        self.btn.pack(side="right")
        self.frameBtn.pack(fill='x')

        # Frame1
        self.frameDisplay = tk.Frame(self)
        self.display_label = tk.Label(self.frameDisplay)
        self.display_label.pack(fill='x')
        self.frameDisplay.pack()



    def changImage(self,imageName):
        print("changImage")

        # img1 = Image.open("./image/{}".format(imageName))
        # print(img1)
        # img1 = img1.resize((self.width,self.height-50), Image.ANTIALIAS)

        img = tk.PhotoImage(file="./image/{}".format(imageName))
        img = img.subsample(2, 2)
        self.display_label.configure(image=img)
        self.display_label.image = img

    def Stop(self):
        print("stop inFrameSlid")
        self.Frame.stop()
        self.destroy()
        self.update()

class SlideShow(threading.Thread):
    def __init__(self, Frame):
        threading.Thread.__init__(self)
        self.Frame = Frame
        self.time = 1
        print("Slidshow class have time variable is ",self.time)
        self.listFileName = []

    def run(self):
        self.time = self.Frame.Time
        try:
            print("running")
            self.listFileName = self.getFileInFolder()
            print("Slidshow class have listFileName variable is ", self.listFileName)
            while True:
                for i in self.listFileName :
                    self.Frame.changImage(i)
                    time.sleep(int(self.time))
        finally:
            print('ended Slidshow')

    def getFileInFolder(self):
        mypath = "./image"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(onlyfiles)
        return onlyfiles

    def stop(self):
        self.raise_exception()
        self.join()
        print("Stop Slidshow")

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


# class Start():
#     def __init__(self,Frame):
#         self.Frame = Frame
#         self.fileName = []
#
#     def getFileInFolder(self):
#         mypath = "./image"
#         onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#         print(onlyfiles)
#         return onlyfiles
#
#     def start(self):
#         self.fileName = self.getFileInFolder()
#         for i in self.fileName :
#             print(i)
#             threading.Timer(self.Frame.Time, self.Frame.changImage, args=(i)).start()