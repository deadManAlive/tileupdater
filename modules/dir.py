# directory manipulation

import os
import re

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

def photosAppDirectory() -> str:
    appPrnt = os.path.join(os.environ['LOCALAPPDATA'], 'Packages')
    photosApp = [dr for dr in os.listdir(appPrnt) if re.search("\\.Photos_", dr)]
    for sDir in photosApp:
        appDir = os.path.join(appPrnt, sDir, 'LocalState', 'PhotosAppTile')
        if os.path.isdir(appDir):
            return appDir
        else:
            return ""
    return ""