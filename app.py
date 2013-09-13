from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from os import listdir, remove
from os.path import isfile, join

app = Flask(__name__)

@app.route('/')
def fileshare():
  files = [ f for f in listdir('files/') if isfile(join('files/',f)) ]
  return render_template('app.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
  f = request.files['file']
  f.save('files/' + secure_filename(f.filename))
  return redirect(url_for('fileshare'))

@app.route('/<filename>')
def download_file(filename):
  return send_from_directory('files/', filename)

@app.route('/delete/<filename>')
def delete_file(filename):
  remove('files/' + filename)
  return redirect(url_for('fileshare'))


if __name__ == '__main__':
  app.run(debug=True)
