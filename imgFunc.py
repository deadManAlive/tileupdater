#########################################
#   function for image renaming(rename) #
#   and croping and resizing(imageCnR)  #
#########################################

import os, PIL, subprocess, re
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

def PhotosAppSeeker():
    subprocess.call('powershell.exe Get-AppxPackage -Name "Microsoft.Windows.Photos" >appsDir.txt', shell=True)
    paDetails = open(os.path.join(os.getcwd(), r'appsDir.txt'))
    installLocation = ''
    for line in paDetails:
        dirSeek = re.search("\AInstallLocation", line)
        if dirSeek:
            _,installLocation = line.strip().split(' : ')
    return installLocation

def stopper():
    raise SystemExit