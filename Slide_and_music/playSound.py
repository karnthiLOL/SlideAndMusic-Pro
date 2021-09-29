from os import listdir
from os.path import isfile, join
import threading
import ctypes
from playsound import playsound
import pygame

class PlaySound(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.listFileName = []
        pygame.mixer.init()

    # def play(self):
    #     pygame.mixer.music.load(
    #         r"C:\Users\karnt\Desktop\ชอบฟัง\สากล\John Denver - Take Me Home, Country Roads (Audio).mp3")
    #     pygame.mixer.music.play(loops=0)


    def run(self):
        try:
            print("running")
            self.listFileName = self.getFileInFolder()
            print("playSound clasNams have listFilee variable is ", self.listFileName)
            for i in self.listFileName :
                pygame.mixer.music.load(r"./sound/{}".format(i))
                pygame.mixer.music.play(loops=-1)
        finally:
            print('ended playsound1')

    def getFileInFolder(self):
        mypath = "./sound"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(onlyfiles)
        return onlyfiles

    def stop(self):
        print("Stop")
        pygame.mixer.music.stop()
        self.raise_exception()
        self.join()
        print("Stop play Sound")

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
