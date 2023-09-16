import PyPDF2



pdfs = ["dummy.pdf" , "sample.pdf"]

merger = PyPDF2.PdfMerger()

for filename in pdfs:
    pdffile = open(filename , 'rb')
    pdf_reader = PyPDF2.PdfReader(pdffile)
    merger.append(pdf_reader)
pdffile.close()
merger.write('merged.pdf')