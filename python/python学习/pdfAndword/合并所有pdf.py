#从多个pdf中合并并选择多个页面
import PyPDF2, os

#Get all the pdf filenames
pdfFiles = []
for filename in os.listdir(r"C:\Users\刘必勇\Desktop\python\pdfAndword"):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
#sort
pdfFiles.sort(key = str.lower)

#pdfwrite
pdfWriter = PyPDF2.PdfFileWriter()

#Loop Throught all pdf files
for filename in  pdfFiles:
    pdfFileObj = open(os.path.join(r"C:\Users\刘必勇\Desktop\python\pdfAndword",filename), "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#loop Throght all pages (except the first)and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
#save
pdfOutputFile = open("allminutes.pdf", "wb")
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
