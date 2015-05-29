# pdfManip
Tools that allow you to manipulate PDFs.



Progress:

	- app.py Flask setup with routes to:
		- / Home page which currently allows for uploading
		- /combine for a page listing current uploaded PDF's in pdfManip/uploads/ folder
		- /uploads/[filename] to view the specific pdf.

	- manip.py has the main logic for combining pdfs with PyPDF2 library


To Do List:
	
	- Add a "combine" button on home page and move to /combine view (and use the /combine view as a confirmation page).
	- Allow to upload multiple files at once.
	- Find a better way to save temporary files before combining them.
	- **important: Find a way to run the python script that combines the pdfs through the click of a button
	- Delete temporary pdf files after combining them
