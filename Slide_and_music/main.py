import tkinter as tk
from toplevel import SetTime as FrameST
from uploadeImage import UploadImage
from Slideshow import SlideShow ,FrameSlid
from uploadeSound import UploadSound
from playSound import PlaySound
from tkinter import messagebox as ms
from tkinter import filedialog as fd
from PIL import Image
import PIL
import os
import threading
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # variable
        self.FrameST = False
        self.Time = 1
        self.imageId = 0

        # model
        self.UploadImage = UploadImage()
        self.UploadSound = UploadSound()
        self.slideShow = False
        self.playSound = False
        self.frameSlid = False

        # config
        self.title("Slide & Music Pro.")
        self.geometry("1200x600")
        self.minsize(1100, 600)
        self.maxsize(1500, 650)
        self.resizable(True, True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.iconbitmap("./sys/icon.ico")

        self.deleteFile()

        pro_title = tk.Label(self, text="\nSlide & Music Pro.", font="100")
        pro_title.grid(row=0, column=0, columnspan=2, sticky="EW")

        # button
        button_1 = tk.PhotoImage(file="./sys/button_1.png")
        button_2 = tk.PhotoImage(file="./sys/button_2.png")
        button_3 = tk.PhotoImage(file="./sys/button_3.png")
        button_4 = tk.PhotoImage(file="./sys/button_4.png")
        button_1 = button_1.subsample(2, 2)
        button_2 = button_2.subsample(2, 2)
        button_3 = button_3.subsample(2, 2)
        button_4 = button_4.subsample(2, 2)
        import_image = tk.Button(self,image=button_1, command= self.uploadImage)
        import_image.image = button_1
        import_image.grid(row=1, column=1, rowspan=1, sticky="nsew", padx=2,
                                                                  pady=2)
        import_mp3 = tk.Button(self,image=button_2, command= self.uploadSound)
        import_mp3.image = button_2
        import_mp3.grid(row=2, column=1, rowspan=1, sticky="nsew", padx=2,
                                                                pady=2)
        Timer = tk.Button(self,image=button_3, command= self.showTime)
        Timer.image = button_3
        Timer.grid(row=3, column=1, rowspan=1, sticky="nsew", padx=2,
                                                                    pady=2)
        Start = tk.Button(self,image=button_4, command= self.start)
        Start.image = button_4
        Start.grid(row=4, column=1, rowspan=1, sticky="nsew", padx=2, pady=2)

        # display
        display = tk.PhotoImage(file="./sys/slide_and_music_banner.png")
        display = display.subsample(2, 2)
        self.display_label = tk.Label(self, image=display)
        self.display_label.image = display
        self.display_label.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=2, pady=2)

    def start(self):
        print("Start")
        if self.checkImage() > 0 and self.checkSound() > 0:
            self.frameSlid = FrameSlid(self)
            self.playSound = PlaySound()
            self.slideShow = SlideShow(self)
            self.playSound.start()
            self.slideShow.start()
        elif self.checkImage() <= 0 :
            ms.showwarning('คำเตือน', 'ไม่พบไฟล์ภาพ')
        elif self.checkSound() <= 0 :
            ms.showwarning('คำเตือน', 'ไม่พบไฟล์เสียง')

    def checkImage(self):
        return len([ i for i in os.listdir("./image")])

    def checkSound(self):
        return len([ i for i in os.listdir("./sound")])

    def deleteFile(self):
        deleteFileInImage = [i for i in os.listdir("./image") if os.remove(os.path.join("./image", i))]
        deleteFileInSound = [i for i in os.listdir("./sound") if os.remove(os.path.join("./sound", i))]

    def stop(self):
        print("Stop")

        threading.Thread(target=self.slideShow.stop).start()
        threading.Thread(target=self.playSound.stop).start()
        # self.slideShow.stop()
        # self.playSound.stop()


    def showTime(self):
        self.FrameST = FrameST(self)

    def setTime(self,data):
        self.Time = data
        print(self.Time)
        self.FrameST.destroy()

    def uploadImage(self):
        print("UploadImage")
        self.UploadImage.open()

    def uploadSound(self):
        print("UploadSound")
        self.UploadSound.open()

    def changImage(self,imageName):
        self.frameSlid.changImage(imageName)

    # def changImage(self,imageName):
    #     img = tk.PhotoImage(file="./image/{}".format(imageName))
    #     img = img.subsample(2, 2)
    #     self.display_label.configure(image=img)
    #     self.display_label.image = img
    #     self.imageId += 1

if __name__ == "__main__":
    app = App()
    app.mainloop()