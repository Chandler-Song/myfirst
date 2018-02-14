import os, shutil

#遍历目录树

def f(name):
    os.makedirs("D:\\newfile")
    for foldernames,subfoldernames,filenames in os.walk(name):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ".png" or os.path.splitext(filename)[1] == ".jpg":
                shutil.copy(os.path.join(foldernames, filename),"D:\\newfile")#这样写如果原目录中无newfile这回认为是文件改名

name = input("please enter a filename:")
f(name)
print("Done")