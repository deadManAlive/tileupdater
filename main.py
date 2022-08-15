from asyncio.log import logger
import os, random, shutil, re
from PIL import Image
import json

# Rename a picture to compatible format
def renamer(path: str) -> None:
    i = 0
    for img in os.listdir(path):
        dst = "Tile" + str(i) + ".jpg"
        src = os.path.join(path, img)
        dst = os.path.join(path, dst)
        os.rename(src, dst)
        # print(src, dst)
        i += 1

# Crop image to square based on minimal dimension of the image
def imageCropAndResize(img: str, src: str, tgt: str) -> None:
    imgpath = os.path.join(src, img)
    imgobj = Image.open(imgpath)
    imgobj.thumbnail((1024, 1024))
    width, height = imgobj.size
    cwidth = cheight = min(imgobj.size)
    imgobj.crop(((width - cwidth) // 2, (height - cheight) // 2, (width + cwidth) // 2, (height + cheight) // 2)).save(os.path.join(tgt, img))

def PhotosAppDirectory() -> str | None:
    appPrnt = os.path.join(os.environ['LOCALAPPDATA'], 'Packages')
    photosApp = [dr for dr in os.listdir(appPrnt) if re.search("\\.Photos_", dr)]
    for sDir in photosApp:
        appDir = os.path.join(appPrnt, sDir, 'LocalState', 'PhotosAppTile')
        if os.path.isdir(appDir):
            return appDir
        else:
            return None

# main function
if __name__ == "__main__":
    config = json.load(open("config.json"))

    cwd = os.path.dirname(__file__)

    if config["usePhotosAppDir"] is False:
        cache = os.path.join(cwd, config["cacheDir"])
        target = os.path.join(cwd, config["targetDir"])
    elif config["usePhotosAppDir"] is True:
        cache = config["cacheDir"]
        target = config["targetDir"]
    else:
        raise Exception("configuration 'useLocalDir' did not set correctly.")

    if not os.path.isdir(cache):
        os.mkdir(cache)
    if not os.path.isdir(target):
        os.mkdir(target)

    for root, dirs, files in os.walk(target):
        for file in files:
            os.remove(os.path.join(target, file))
    for root, dirs, files in os.walk(cache):
        for file in files:
            os.remove(os.path.join(cache, file))

    seeker = []

    for dir in config["picDirPaths"]:
        if os.path.isdir(dir):
            print("Processing images in {}...".format(dir))
            seeker.extend(
                sorted(
                    [
                        os.path.join(root, f) for root, _, files in os.walk(dir) for f in files if (f.lower().endswith(".jpg") or f.lower().endswith(".jpeg"))
                    ],
                    key=os.path.getctime,
                    reverse=True
                )
            )
        else:
            print("Not processing {}: is not a directory!".format(dir))
    
    seeker = random.sample(seeker, k=5)

    for img in seeker:
        shutil.copy(img, cache)

    renamer(cache)

    for img in os.listdir(cache):
        imageCropAndResize(img, cache, target)