import bottle
import argparse
import os
import functools

HTML_UPLOAD_PAGE = "PyFiUp.html"
JS_FILE = "PyFiUp.js"
CSS_FILE = "PyFiUp.css"
DIRECTORY_UPLOAD = "uploads"

KEY_UPLOADED_FILE = "file"

def make_dir(directory_name):
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        pass
    except Exception as e:
        print("Exception occurred when making a direcotry: " + str(e))
        exit()

@bottle.get("/upload")
def get_upload_page():
    return bottle.static_file(HTML_UPLOAD_PAGE, root=".")

@bottle.get("/"+JS_FILE)
def get_js():
    return bottle.static_file(JS_FILE, root=".")

@bottle.get("/"+CSS_FILE)
def get_css():
    return bottle.static_file(CSS_FILE, root=".")

@bottle.post("/upload")
def upload_file():
    make_dir(DIRECTORY_UPLOAD)
    uploaded_file = bottle.request.files.get(KEY_UPLOADED_FILE)
    file_name_test = uploaded_file.filename
    file_name_test_increment = 0
    while os.path.isfile(os.path.join(DIRECTORY_UPLOAD, file_name_test)):
        file_name_test_increment = file_name_test_increment + 1
        if "." in file_name_test:
            file_name_separated = uploaded_file.filename.split(".")
            file_name_separated[0] = file_name_separated[0] + str(file_name_test_increment)
            file_name_test = functools.reduce(lambda s1, s2 : s1 + "." + s2, file_name_separated)
        else:
            file_name_test = uploaded_file.filename + str(file_name_test_increment)
    uploaded_file.filename = file_name_test
    # For file names, Bottle changes spaces to dashes, and deletes parantheses.
    uploaded_file.save(DIRECTORY_UPLOAD, overwrite=False)

parser = argparse.ArgumentParser()
parser.add_argument("--interface", metavar="i", type=str, default="0.0.0.0", help="The interface the website will bind to. Defaults to 0.0.0.0 (all interfaces)")
parser.add_argument("--port", metavar="p", type=int, default=9337, help="The port the website will bind to. Defaults to 9337")
parser.add_argument("--output", metavar="o", type=str, default=DIRECTORY_UPLOAD, help="The directory path where uploaded files are stored")

args = parser.parse_args()
DIRECTORY_UPLOAD = os.path.abspath(args.output)

bottle.run(host=args.interface, port=args.port)