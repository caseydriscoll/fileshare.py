from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from os import listdir
from os.path import isfile, join


app = Flask(__name__)

@app.route('/')
def fileshare():
  files = [ f for f in listdir('uploads/') if isfile(join('uploads/',f)) ]
  return render_template('app.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
  f = request.files['file']
  f.save('uploads/' + secure_filename(f.filename))
  return redirect(url_for('fileshare'))

if __name__ == '__main__':
  app.run('0.0.0.0')
