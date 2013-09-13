from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def fileshare():
  return render_template('app.html')

@app.route('/upload', methods=['POST'])
def upload_file():
  f = request.files['file']
  f.save('uploads/' + secure_filename(f.filename))
  return render_template('app.html')

if __name__ == '__main__':
  app.run('0.0.0.0')
