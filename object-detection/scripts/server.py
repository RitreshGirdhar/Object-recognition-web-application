from flask import (
    Flask,
    render_template,
    request,
    send_from_directory
)
import logging, os
import Detection1

# Create the application instance
app = Flask(__name__, template_folder="templates")
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/detect', methods = ['POST'])
def detect():
    if request.method == 'POST' and request.files['image']:
    	img_name = request.files['image']
    	create_new_folder(app.config['UPLOAD_FOLDER'])
    	saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    	app.logger.info("saving {}".format(saved_path))
    	img_name.save(saved_path)
    	Detection1.detectObject()
    	return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)
    else:
    	return "Where is the image?"


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)