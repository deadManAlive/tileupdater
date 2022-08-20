# image manipulation

import os
from PIL import Image

# Crop image to square based on minimal dimension of the image
def imageCropAndResize(img: str, src: str, tgt: str) -> None:
    imgpath = os.path.join(src, img)
    imgobj = Image.open(imgpath)
    imgobj.thumbnail((1024, 1024))
    width, height = imgobj.size
    cwidth = cheight = min(imgobj.size)
    imgobj.crop(((width - cwidth) // 2, (height - cheight) // 2, (width + cwidth) // 2, (height + cheight) // 2)).save(os.path.join(tgt, img))
