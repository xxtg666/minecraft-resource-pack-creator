import os
from PIL import Image
def iif(f):
    return f.endswith(".png")
def rep(dir):
    l=os.listdir(dir)
    for i in l:
        if os.path.isdir(dir+"/"+i):
            rep(dir+"/"+i)
        if iif(i):
            img=Image.open(dir+"/"+i)
            w=img.width
            h=img.height
            tmp_example=example.resize((w,h))
            tmp_example.save(dir+"/"+i)
            print(dir+"/"+i)