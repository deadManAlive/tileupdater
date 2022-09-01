import os
import random
import shutil
import json

from modules.directories import photosAppDirectory, renamer
from modules.images import imageCropAndResize
from modules.layout import restart as rs # needs admin. priv.

# main function
if __name__ == "__main__":
    config = json.load(open("config.json"))

    cwd = os.path.dirname(__file__)

    """
        if 'usePhotosAppDir' is `true`
            -> 'target' is from 'PhotosAppDirectory()'
            -> 'cache' is from cacheDir
        else
            -> 'target' and 'cache' from config.json

        throw err if target and cache could not be found.
    """

    if config["usePhotosAppDir"] is False:
        print("[LOCAL MODE]")
        cache = os.path.join(cwd, config["cacheDir"])
        target = os.path.join(cwd, config["targetDir"])
    elif config["usePhotosAppDir"] is True:
        print("[ON APP DIR]")
        cache = os.path.join(cwd, config["cacheDir"])
        target = photosAppDirectory()

        print("Photos app tile folder found at {}.".format(target))
    else:
        raise Exception("`usePhotosAppDir` (bool) in `config.json` did not set correctly.")

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

    # rs(cwd)