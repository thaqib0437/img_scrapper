from PIL import Image, ImageFilter 
import numpy as np
import os
####
class imgHandler(object):
    def __init__(self, download_folder, dirc, delete_prev = False):
        self.download_folder = download_folder
        self.dirc = str(dirc) + '/' + self.download_folder
        self.images = os.listdir(self.dirc)  
        self.delete_prev = delete_prev
    def resize(self,*size):
        os.chdir(self.dirc)
        if(len(size) is not 2 and size is not isinstance(size,int)):
            print("Size not valid \n  USAGE: imgHandler.resize(x,y) x,y are ints \n ")
            return 404
        print(os.getcwd())
        for image in self.images:
            img = Image.open(image)
            new_img = img.resize(size)
            if (self.delete_prev):
                try:
                    name = image
                    os.remove(image)
                    new_img.save(name)
                except:
                    pass
                pass
            else:
                new_img.save(str(size) + '_' + image)
        return 0
    #TODO geckodriver download locally
    def greyScale(self,*size):
        os.chdir(self.dirc)
        if(len(size) is not 2 and size is not isinstance(size,int)):
            print("Size not valid \n  USAGE: imgHandler.resize(x,y) x,y are ints \n ")
            return 404
        print(os.getcwd())
        for image in self.images:
            img = Image.open(image)
            img = img.convert('L')
            new_img = img.resize(size)
            if (self.delete_prev):
                try:
                    name = image
                    os.remove(image)
                    new_img.save(name)
                except:
                    pass
                pass
            else:
                new_img.save(str(size) + '_' + image)
        return 0
    def edgeDetect(self,*size):
        os.chdir(self.dirc)
        if(len(size) is not 2 and size is not isinstance(size,int)):
            print("Size not valid \n  USAGE: imgHandler.resize(x,y) x,y are ints \n ")
            return 404
        print(os.getcwd())
        for image in self.images:

            img = Image.open(image)
            img = img.convert("L")
            img = img.filter(ImageFilter.FIND_EDGES)
            new_img = img.resize(size)
            if (self.delete_prev):
                try:
                    name = image
                    os.remove(image)
                    new_img.save(name)
                except:
                    pass
                pass
            else:
                new_img.save(str(size) + '_' + image)
        return 0

    #TODO geckodriver download locally, custom kernel
    




