from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    send_file
)
from flask import jsonify
import logging, os
import Detection


# Create the application instance
app = Flask(__name__, template_folder="./templates")
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
SRC_FOLDER = '{}/source/'.format(PROJECT_HOME)
DEST_FOLDER = '{}/dest/'.format(PROJECT_HOME)
app.config['SRC_FOLDER'] = SRC_FOLDER
app.config['DEST_FOLDER'] = DEST_FOLDER

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_image/<folder>/<section>')
def get_image(folder,section):
    return send_file("/app/"+folder+"/"+section, mimetype='image/gif')

@app.route('/detect', methods = ['POST'])
def detect():
    if request.method == 'POST' and request.files['image']:
        img = request.files['image']
        img_name = img.filename
        create_new_folder(app.config['SRC_FOLDER'])
        create_new_folder(app.config['DEST_FOLDER'])
        saved_path = os.path.join(app.config['SRC_FOLDER'], img_name)
        saved_path1 = os.path.join(app.config['DEST_FOLDER'], img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        img.save(saved_path1)
        detections = Detection.detectObject(saved_path,saved_path1)
        strings2 = list()
        for eachObject in detections:
               strings2.append(eachObject["name"] + " : " + "{:10.2f}".format(eachObject["percentage_probability"]))
        return render_template('result.html',sourceImage=img_name,newImage=img_name,data=strings2)
    else:
    	return "Where is the image?"

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, port=80)