import zipfile, os

def backupToZip(folder):
    # Back the entire contents of folder into a zip file
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1
# creat a zip file
    print("Creating %s..."%(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,"w")
    print("Done.")

    for foldername,subfoldername,filenames in os.walk(folder):
        print("Adding files in %s..." % (foldername))
        backupZip.write(foldername)#添加某个文件夹里的文件部分
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endsname(".zip"):
                continue
            backupZip.write(os.path.join(foldername, filename))
            backupZip.close()
            print("Done")




