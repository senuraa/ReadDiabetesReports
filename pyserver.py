from flasgger import Swagger
from flask import Flask
from flask_restful import Api
import os
import extract_text
import utils
from flask_cors import CORS

# utils.check_dir_exist('cropped-imgs')
# utils.check_dir_exist('hocr-files')
# utils.check_dir_exist('img-origin')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/ReadDiabetesReports/google-service-account.json"
utils.create_dir("cropped-imgs")
utils.create_dir("hocr-files")
utils.create_dir("img-origin")
app = Flask(__name__)
CORS(app,resources={r"/api/*": {"origins": "*"}})
template = {
    "info": {
        "title": "OCR ENGINE for health reports",
        "description": "Retrieve information from health reports for diagnosis, version-1 ",
        "version": "1.0"
    },
    "host": "http://localhost:5001",
    "basePath": "/api",  # base bash for blueprint registration
}
api = Api(app)
Swagger = Swagger(app, template=template)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
api.add_resource(extract_text.ReadImage, '/api/readimage', methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)
