#旋转页面
import PyPDF2
File1 = open("meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(File1)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultFile = open("rotatePage.pdf", "wb")
pdfWriter.write(resultFile)
resultFile.close()
File1.close()