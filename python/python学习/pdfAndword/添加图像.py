#添加图像
import docx
doc = docx.Document()
doc.add_picture("zophie.png", width = docx.shared.Inches(1), height = docx.shared.Cm(4))
doc.save("twoPage.docx")