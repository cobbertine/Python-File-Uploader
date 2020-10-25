import bottle
import argparse
import os

HTML_UPLOAD_PAGE = "PyUp.html"
JS_FILE = "PyUp.js"
CSS_FILE = "PyUp.css"
DIRECTORY_UPLOAD = "./uploads"

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
    file = bottle.request.files.get(KEY_UPLOADED_FILE)
    file_name = file.filename
    file_name_increment = 0
    while os.path.isfile(DIRECTORY_UPLOAD+"/"+file_name):
        file_name_increment = file_name_increment + 1
        file_name = file.filename + str(file_name_increment)
    file.filename = file_name
    # For file names, Bottle changes spaces to dashes, and deletes parantheses.
    file.save(DIRECTORY_UPLOAD+"/", overwrite=False)

parser = argparse.ArgumentParser()
parser.add_argument("--interface", metavar="i", type=str, default="0.0.0.0", help="The interface the website will bind to. Defaults to 0.0.0.0 (all interfaces)")
parser.add_argument("--port", metavar="p", type=int, default=9337, help="The port the website will bind to. Defaults to 9337")

args = parser.parse_args()

bottle.run(host=args.interface, port=args.port)