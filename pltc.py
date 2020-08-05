from imgFunc import renamer, imageCnR, stopper, PhotosAppSeeker
import os, shutil, subprocess


path = os.path.join(os.environ['USERPROFILE'], 'Pictures')

cache= os.path.join(os.getcwd(), r'cache')

target = PhotosAppSeeker()
for _,_,oldTiles in os.walk(target):
    if oldTiles:
        for oldTile in oldTiles:
            os.remove(os.path.join(target, oldTile))

if not os.path.exists(cache):
    os.makedirs(cache)

files = sorted([os.path.join(root,f) for root,_,the_files in os.walk(path) for f in the_files if (f.lower().endswith(".jpg") or f.lower().endswith(".jpeg"))], key=os.path.getctime, reverse = True)

del files[5:]

for _, _, imgs in os.walk(cache):
    if imgs:
        for oldImg in imgs:
            os.remove(os.path.join(cache, oldImg))

for image in files:
    shutil.copy(image, cache)

renamer(cache)

cacheList = os.listdir(cache)

for image in cacheList:
    imageCnR(image, cache, target)