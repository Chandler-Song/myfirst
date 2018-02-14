#拷贝页面
import PyPDF2
pdf1File = open("meetingminutes.pdf", "rb")
pdf2File = open("meetingminutes2.pdf", "rb")
pdf1Read = PyPDF2.PdfFileReader(pdf1File)
pdf2Read = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum  in range(pdf1Read.numPages):
    pageObj = pdf1Read.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum  in range(pdf2Read.numPages):
    pageObj = pdf2Read.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile = open("combineminutes.pdf", "wb")
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()