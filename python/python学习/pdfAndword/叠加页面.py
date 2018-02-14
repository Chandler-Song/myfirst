#叠加页面
import PyPDF2
File1 = open("meetingminutes.pdf", "rb")
pdfReader1 = PyPDF2.PdfFileReader(File1)
page = pdfReader1.getPage(0)
pdfReader2 = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))
page.mergePage(pdfReader2.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
for pagenum in range(1, pdfReader1.numPages):
    pageObj = pdfReader1.getPage(pagenum)
    pdfWriter.addPage(pageObj)
resultFile = open("watermarkedCover.pdf", "wb")
pdfWriter.write(resultFile)
resultFile.close()
File1.close()
