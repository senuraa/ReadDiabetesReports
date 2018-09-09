
import os
from pytesseract import pytesseract
from libs import hocr_search, utils, google_vision
from PIL import Image
import base64
from io import BytesIO
filename = 'img.jpg'

# #TODO:create a function out of this
#TODO:This has to be wrapped with flask
reader_module_path = os.path.dirname(__file__)
session_filename = utils.get_current_time();
hocr_filepath = os.path.join(reader_module_path, 'hocr-files/'+session_filename)
print(hocr_filepath)
pytesseract.run_tesseract(filename, hocr_filepath, extension="box", lang=None, config="hocr --psm 7 tessedit_char_whitelist=0123456789")
search_terms = ("fasting", "blood", "sugar")
hocr_result = hocr_search.parse_hocr(search_terms, hocr_filepath+'.hocr')
ori_image = Image.open(filename)
print(hocr_result)
img_width, img_height = ori_image.size
cropped_image = ori_image.crop(utils.calc_result_box(hocr_result, img_width))
cropped_img_fp = os.path.join(reader_module_path,'cropped-imgs/')
cropped_image.save(cropped_img_fp+session_filename+".jpg", "jpeg")
print(cropped_img_fp)
response = google_vision.get_value(cropped_img_fp+session_filename+".jpg")
print(response)
cropped_image.show();

#print(hocr_result["fasting"])
