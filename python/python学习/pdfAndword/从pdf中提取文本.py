#从pdf文档中提取文本
import PyPDF2
pdfFileObj = open("meetingminutes.pdf","rb")
pdfRead = PyPDF2.PdfFileReader(pdfFileObj)
pdfRead.numPages
pagesObj = pdfRead.getPage(0)
pagesObj.extractText()