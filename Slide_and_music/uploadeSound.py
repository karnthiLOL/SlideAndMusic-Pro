from tkinter import filedialog as fd
from PIL import Image
import datetime
from shutil import copy
import os

class UploadSound():

    def __init__(self):
        self.sound = False

    def open(self):
        file = fd.askopenfilename(
            title="Choose a file",
            filetypes=[
                ('Sound files', ('.mp3')),
            ]
        )
        if file != '' :
            self.sound = file
            print(self.sound)
            self.save()

    def save(self):
        copy(self.sound,os.path.join(os.getcwd(),'sound'))
        print("File copied successfully.")



