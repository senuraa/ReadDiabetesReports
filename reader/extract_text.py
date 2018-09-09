
import os
from pytesseract import pytesseract
from libs import hocr_search, utils, google_vision
from PIL import Image
import base64
from io import BytesIO
from flask import request
from flask_restful import Resource


class ReadImage(Resource):

    def post(self):
        """
        Retrieve corresponding value from the test report.
        ---
        tags:
            - OCR
        parameters:
            - in: body
              name: image
              type: string
              required: true
              example: R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
            - in: body
              name: search_terms
              type: array
              items:
               type: string
              required: true
              example: ["fasting","blood","sugar"]
        responses:
            200:
                description: A corresponding value has been extracted successfully
                properties:
                    extracted_value:
                    type: string
                    description: Retrieved value from the report
        """
        req = request.get_json(force=True)
        if not req.get("image") or not req.get("search_terms"):
            return "Invalid image or search terms"
        session_filename = utils.get_current_time();
        reader_module_path = os.path.dirname(__file__)
        origin_img_base64 = req["image"]
        origin_img_fp = os.path.join(reader_module_path,'img-origin/'+session_filename+'.jpg')

        origin_img = Image.open(BytesIO(base64.b64decode(origin_img_base64)))
        origin_img.save(origin_img_fp)
        hocr_filepath = os.path.join(reader_module_path, 'hocr-files/'+session_filename)
        pytesseract.run_tesseract(origin_img_fp, hocr_filepath, extension="box", lang=None, config="hocr --psm 7 tessedit_char_whitelist=0123456789")

        search_terms = tuple(req["search_terms"])
        #print(search_terms)
        hocr_result = hocr_search.parse_hocr(search_terms, hocr_filepath + '.hocr')
        #print(hocr_result)
        img_width, img_height = origin_img.size
        cropped_image = origin_img.crop(utils.calc_result_box(hocr_result, img_width))
        cropped_img_fp = os.path.join(reader_module_path,'cropped-imgs/')
        cropped_image.save(cropped_img_fp+session_filename+".jpg", "jpeg")
        response = google_vision.get_value(cropped_img_fp+session_filename+".jpg")
        cropped_image.show()
        res_detail = {"extracted_value":response}
        return (res_detail)

