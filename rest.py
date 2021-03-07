# web-app for API image manipulation

Mr lacheheb otman G612277 from flask import Flask, request, render_template, send_from_directory,jsonify
import os
import numpy as np
import sys
from PIL import Image
from test_python import test_

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

sys.path.append("..")


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 500 status explicitly
    return jsonify(Success=False,Error='please check fileformat')
    #return render_template('500.html'), 500


# default access page
@app.route("/")
def main():
    return render_template('index.html')


# upload selected image and forward to processing page
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/images/')

    # create image directory if not found
    if not os.path.isdir(target):
        os.mkdir(target)

    upload_1 = request.files.getlist("file_1")[0]
    filename_1 = upload_1.filename
    ext = os.path.splitext(filename_1)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp") or (ext == ".jpeg") \
            or (ext == ".JPG") or (ext == ".PNG") or (ext == ".BMP") or (ext == ".JPEG"):
        print("File accepted")
    else:
        return render_template("error.html", message="The selected file is not supported"), 400
    destination_1 = "/".join([target, filename_1])
    upload_1.save(destination_1)
    # if len(request.files.getlist("file_2")) > 0:
    upload_2 = request.files.getlist("file_2")[0]
    filename_2 = upload_2.filename
    ext = os.path.splitext(filename_2)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp") or (ext == ".jpeg") \
            or (ext == ".JPG") or (ext == ".PNG") or (ext == ".BMP") or (ext == ".JPEG"):
        print("File accepted")
    else:
        return render_template("error.html", message="The selected file is not supported"), 400
    destination_2 = "/".join([target, filename_2])
    upload_2.save(destination_2)        

        # forward to processing page
    return render_template("processing.html", image_name_1=filename_1, image_name_2=filename_2)


@app.route("/results", methods=["POST"])
def results():
    filename_1 = request.form["image_1"]
    filename_2 = request.form["image_2"]

    target = os.path.join(APP_ROOT, 'static/images')
    destination_1 = "/".join([target, filename_1])
    destination_2 = "/".join([target, filename_2])

    image_res = test_(destination_1,destination_2)

    filename_res = 'res-' + filename_1.split('.')[0]+"_+_"+filename_2
    destination_res = "/".join([target, filename_res])
    if os.path.isfile(destination_res):
        os.remove(destination_res)

    image_res.save(destination_res)
    return render_template("results.html", image_name_1=filename_1, image_name_2=filename_2, image_name_3=filename_res)

# retrieve file from 'static/images' directory
@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=False)

