#########################################
#   function for image renaming(rename) #
#   and croping and resizing(imageCnR)  #
#########################################

import os, PIL
from PIL import Image

def renamer(pather):
    i=0
    for image in os.listdir(pather):
        dst = "Tile" + str(i) + ".jpg"
        src = os.path.join(pather, image)
        dst = os.path.join(pather, dst)
        os.rename(src, dst)
        i += 1


def imageCnR(img, src, tgt):
    imgPath = os.path.join(src, img)
    im = Image.open(imgPath)
    im = im.convert('RGB')
    im.thumbnail((1024, 1024))
    width, height = im.size
    cwidth, cheight = min(im.size), min(im.size)
    im.crop(((width - cwidth) // 2, (height - cheight) // 2, (width + cwidth) // 2, (height + cheight) // 2)).save(os.path.join(tgt, img), quality = 95)

def stopper():
    raise SystemExit