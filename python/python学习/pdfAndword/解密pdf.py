#揭秘pdf
import PyPDF2
pdfFileObj = open("encrypted.pdf","rb")
pdfRead = PyPDF2.PdfFileReader(pdfFileObj)
pdfRead.isEncrypted
#pdfRead.getPage(0)
pdfRead.decrypt("rosebud")#返回0说明密码错误
pageObject = pdfRead.getPage(0)
print(pageObject.extractText())