# start menu layout manipulation
import os
import subprocess
import shutil
import xml.dom.minidom as xmd
import re
import ctypes

# restart start layout by Import-StartLayout (powershell)
def restart(cwd: str):
    # priv. check
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        raise Exception("Start menu manipulation needs admin. privileges!")

    #find powershell
    shell = shutil.which("pwsh")
    shell = shutil.which("powershell") if shell is None else shell

    if shell is None:
        raise Exception("poweshell could not be found in PATH")

    xmlout = os.path.join(cwd, "layout.xml")
    subprocess.call("\"{}\" -command Export-StartLayout -UseDesktopApplicationID -Path {}".format(shell, xmlout), shell=True)

    # xml processing
    attr = ("Size", "Column", "Row", "AppUserModelID")

    doc: xmd.Document = xmd.parse(xmlout)
    apptiles = doc.getElementsByTagName("start:Tile")

    

    for el in apptiles:
        modelId = el.getAttribute("AppUserModelID")

        if re.search("\\.Windows.Photos", modelId):
            print(el)
            for at in attr:
                print("\t{}: {}".format(at, el.getAttribute(at)))

