from google.cloud import vision
import io
import re

def get_value(img_filepath):
    with io.open(img_filepath, 'rb') as image_file:
        content = image_file.read()
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image(content=content)
    res = client.text_detection(image=image)
    texts = res.text_annotations

    for text in texts:
        org_value = '\n"{}"'.format(text.description)
        break
    final_val = re.sub("[^0-9.]", "", org_value)
    return final_val
