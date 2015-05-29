from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug import secure_filename
import os, glob

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		if f and allowed_file(f.filename):
			filename = secure_filename(f.filename)
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/combine')
def combine():
	files = []
	cd = os.getcwd()
	print(cd[len(cd)-7:])
	if cd[len(cd) - 7:] == "uploads":
		os.chdir("../uploads")
	else:
		os.chdir("../pdfManip/uploads")
	for f in glob.glob("*.pdf"):
		print(f)
		files.append(f)
	return render_template("combine.html", filenames = files)

if __name__ == '__main__':
	app.run(debug=True)