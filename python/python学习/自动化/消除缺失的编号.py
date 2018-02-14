import os, shutil, re

#遍历目录树

def f(name):
    num = []
    renum = re.compile(r"\d.*")
    for foldername,subfoldernames,filenames in os.walk(name):
        for filename in filenames:
            num.append(int((renum.findall(os.path.splitext(os.path.join(foldername, filename))[0][4:]))[0]))
    num.sort()
    for i in range(len(num)):
        for foldername, subfoldernames, filenames in os.walk(name):
            for filename in filenames:
                if int((renum.findall(os.path.splitext(os.path.join(foldername, filename))[0][4:]))[0]) == num[i]:
                    shutil.move(os.path.join(foldername, filename),os.path.join(foldername,os.path.splitext(filename)[0][:4] + ("00" + str(i))[-3:] + ".txt"))

name = input("please enter a filename:")
f(name)
print("Done")