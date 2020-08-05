from imgFunc import renamer, imageCnR, stopper, PhotosAppSeeker
import os, shutil, subprocess


path = os.path.join(os.environ['USERPROFILE'], 'Pictures')

cache, target = os.path.join(os.getcwd(), r'cache'), os.path.join(os.getcwd(), r'target')

realT = PhotosAppSeeker()
realT = os.path.join(realT, 'LocalState', 'PhotosAppTile')
print(realT)    ###THIS IS NOT THE DIR WE LOOKING FOR ###
print(os.path.exists(realT))

if not os.path.exists(cache):
    os.makedirs(cache)
if not os.path.exists(target):
    os.makedirs(target)

for _, _, imgs in os.walk(target):
    if imgs:
        for img in imgs:
            os.remove(os.path.join(target, img))
        

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