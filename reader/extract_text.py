import difflib
import cv2
from pytesseract import pytesseract
from libs import hocr_search
from bs4 import BeautifulSoup as bs
filename = 'img.jpg'

# # read the image and get the dimensions
# img = cv2.imread(filename)
# h, w, _ = img.shape  # assumes color image
#
# # run tesseract, returning the bounding boxes
# boxes = pytesseract.image_to_boxes(img)  # also include any config options you use
# print(boxes);
# # draw the bounding boxes on the image
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
#
# # show annotated image and wait for keypress
# cv2.imshow(filename, img)
# cv2.waitKey(0)
# # def get_boxes():
# #TODO:create a function out of this
#TODO:This has to be wrapped with flask
pytesseract.run_tesseract(filename, 'output', extension="box", lang=None, config="hocr")
search_terms = ("fasting blood sugar","serum creatinine")
hocr_result = hocr_search.parse_hocr(search_terms, 'output.hocr')
print(hocr_result)
