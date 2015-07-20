import xml.etree.ElementTree as ET
import os

dirDecodeEncoding = "gbk";
 
def GetFileList(dir, fileList):
    newDir = dir
    # if dir is file and filename extension is xml
    if os.path.isfile(dir) and dir.decode(dirDecodeEncoding).endswith(".xml") and os.path.dirname(dir).endswith("\layout"):
        fileList.append(dir.decode(dirDecodeEncoding))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            # ignore generated folder an hidden folder
            if s == "build" or s == "gen" or s.startswith("."):
                continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList;
 
def addFitsSystemWindows(filePath):
    ET.register_namespace("android", "http://schemas.android.com/apk/res/android")
    with open(filePath, "r") as handle:
        root = ET.parse(handle)
    try:
        isSet = root.getroot().attrib["{http://schemas.android.com/apk/res/android}fitsSystemWindows"];
        if isSet == false:
            raise Exception
    except Exception, e:
        root.getroot().attrib["{http://schemas.android.com/apk/res/android}fitsSystemWindows"] = "true"
    root.write(filePath, encoding='utf-8', xml_declaration=True)

list = GetFileList(os.getcwd(), [])
for filePath in list:
    addFitsSystemWindows(filePath);