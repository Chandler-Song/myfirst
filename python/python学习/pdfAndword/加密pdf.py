#加密pdf
import PyPDF2
File1 = open("meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(File1)
pdfWriter = PyPDF2.PdfFileWriter()
for pagenum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pagenum)
    pdfWriter.addPage(pageObj)
pdfWriter.encrypt("liuboyong")
resultFile = open("myencryptedminutes.pdf", "wb")
pdfWriter.write(resultFile)
resultFile.close()
File1.close()
