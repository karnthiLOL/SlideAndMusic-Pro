import os

deleteFileInImage = [i for i in os.listdir("./image") if os.remove(os.path.join("./image",i))]
deleteFileInSound = [i for i in os.listdir("./sound") if os.remove(os.path.join("./sound",i))]

