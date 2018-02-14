import shutil, os, re

#Creat a regex that matches files with the American MM-DD-YYYY dates format
# to European DD-MM-YYYY
datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

#Loop over the files in working directory.
for amerFilename in os.listdir("."):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.groups(1)
    monthPart = mo.groups(2)
    dayPart = mo.groups(4)
    yearPart = mo.groups(6)
    afterPart = mo.groups(8)

#Form the European-style filename
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
    absWorkingDir = os.path.abspath(".")
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #重命名文件
    print("Renaming %s to %s...",%(amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)