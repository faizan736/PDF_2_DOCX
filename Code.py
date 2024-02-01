#pdf to document
from pdf2docx import Converter
old_pdf="nameofthe.pdf"
new_doc="new.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()


#documnet to pdf
from docx2pdf import convert
convert("new.docx","new.pdf")
