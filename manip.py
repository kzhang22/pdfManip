import PyPDF2
import sys


#Initialization

#list of pdf names
pdflist = []
pdfWriter = PyPDF2.PdfFileWriter()

for i in range(len(sys.argv)-1):
	pdflist.append(sys.argv[i+1])

first_pdfname = pdflist.pop(0)
first_pdf = open(first_pdfname, 'rb')
first_pdfReader = PyPDF2.PdfFileReader(first_pdf)

for page_num in range(first_pdfReader.numPages):
	page = first_pdfReader.getPage(page_num)
	pdfWriter.addPage(page)

#list of pdf File objects
pdf_files = []

for pdfname in pdflist:
	pdf = open(pdfname, 'rb')
	pdf_files.append(pdf)
	pdfReader = PyPDF2.PdfFileReader(pdf)

	for page_num in range(pdfReader.numPages):
		page = pdfReader.getPage(page_num)
		pdfWriter.addPage(page)


pdf_output = open('combinedfile_' + first_pdfname, 'wb')
pdfWriter.write(pdf_output)
pdf_output.close()

first_pdf.close()

for pdf in pdf_files:
	pdf.close()

