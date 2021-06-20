import PIL
from PIL import Image
import os

myWidth=1920
source='/home/thor/Desktop/Me'
destination='/home/thor/Desktop/compressed_me'


def compress(old_pic, new_pic, myWidth):
    img=Image.open(old_pic)
    wpercent=(myWidth/float(img.size[0]))
    hsize=int((float(img.size[1])*float(wpercent)))
    img=img.resize((myWidth,hsize), PIL.Image.ANTIALIAS)
    img.save(new_pic)

def recursive_compress(source, destination, width):
    files=os.listdir(source)
    for file in files:
        old_pic=source+'/'+file
        new_pic=destination+'/'+file
        compress(old_pic, new_pic, width)
        print(file,"Done")

recursive_compress(source, destination, myWidth)