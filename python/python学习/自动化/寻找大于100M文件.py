import os, shutil

#遍历目录树

def f(name):
    for foldername,subfoldernames,filenames in os.walk(name):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) > 100 * 1024 * 1024:
                print(os.path.join(foldername, filename))

name = input("please enter a filename:")
f(name)
print("Done")