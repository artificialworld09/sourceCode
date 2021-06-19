import PIL
from PIL import Image

myWidth=3264

img=Image.open('me.jpg')
wpercent=(myWidth/float(img.size[0]))
hsize=int((float(img.size[1])*float(wpercent)))
img=img.resize((myWidth,hsize), PIL.Image.ANTIALIAS)
img.save('resized.jpg')