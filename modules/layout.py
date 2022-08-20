# start menu layout manipulation
import os
import subprocess
import shutil
import xml.etree.ElementTree as xt

def reStart(cwd: str):
    #find powershell
    shell = shutil.which("pwsh")
    shell = shutil.which("powershell") if shell is None else shell

    if shell is None:
        raise Exception("poweshell could not be found in PATH")

    xmlout = os.path.join(cwd, "layout.xml")
    subprocess.call("\"{}\" -command Export-StartLayout -UseDesktopApplicationID -Path {}".format(shell, xmlout), shell=True)

    # xml processing
    ltree = xt.parse(xmlout)

    print("root: {}".format(ltree.getroot()))
