import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image
import datetime

class UploadImage():

    def __init__(self):
        self.image = False

    def open(self):
        file = fd.askopenfilename(
            title="Choose a file",
            filetypes=[
               ('image files', ('.png', '.jpg')),
           ])
        if file != '' :
            self.image = Image.open(r"{}".format(file))
            self.save()

    def save(self):
        x = datetime.datetime.now()
        x = x.strftime("%H-%M-%S-%f")
        self.image.save(r"./image/{}.png".format(x))



