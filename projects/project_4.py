import PyPDF2



pdfs = ["new copy1.pdf" , "newOne.pdf"]

merger = PyPDF2.PdfMerger()

for filename in pdfs:
    pdffile = open(filename , 'rb')
    pdf_reader = PyPDF2.PdfReader(pdffile)
    merger.append(pdf_reader)
pdffile.close()
merger.write('main.pdf')