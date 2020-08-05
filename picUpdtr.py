import os, random, shutil, PIL
from PIL import Image

def renamer(path):
    i=0
    for image in os.listdir(path):
        dst = "Tile" + str(i) + ".jpg"
        src = cache + image
        dst = cache + dst
        os.rename(src, dst)
        i += 1


def imageCnR(img, src, tgt):
    imgPath = os.path.join(src, img)
    im = Image.open(imgPath)
    im.thumbnail((1024, 1024))
    width, height = im.size
    cwidth, cheight = min(im.size), min(im.size)
    im.crop(((width - cwidth) // 2, (height - cheight) // 2, (width + cwidth) // 2, (height + cheight) // 2)).save(os.path.join(tgt, img), quality = 95)


path, path2 = "/Users/root/Pictures/wpp/", "D://pax aeterna"
cache = "/Users/root/Desktop/null_/piclivCgr/cache/"
target = "/Users/root/Desktop/null_/piclivCgr/PAT/"

for root, dirs, files in os.walk(target):
    for file in files:
        os.remove(os.path.join(target, file))
        

files = sorted([os.path.join(root,f) for root,_,the_files in os.walk(path) for f in the_files if (f.lower().endswith(".jpg") or f.lower().endswith(".jpeg"))], key=os.path.getctime, reverse = True)
files2= sorted([os.path.join(root,f) for root,_,the_files in os.walk(path2) for f in the_files if (f.lower().endswith(".jpg") or f.lower().endswith(".jpeg"))], key=os.path.getctime, reverse = True)

# del files[50:]
# del files2[50:]

seeker = files + files2
# seeker.sort(key=os.path.getctime, reverse=True)

seekerR = random.sample(seeker, k=5)

os.system('rmdir /S /Q cache')
os.system('mkdir cache')

for image in seekerR:
    shutil.copy(image, cache)

renamer(cache)

cacheList = os.listdir(cache)

for image in cacheList:
    imageCnR(image, cache, target)