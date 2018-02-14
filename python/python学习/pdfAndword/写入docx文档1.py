#写入docx文档1
import docx
doc = docx.Document("demo.docx")
doc.add_paragraph("Hello world!")
doc.save("helloworld.docx")
