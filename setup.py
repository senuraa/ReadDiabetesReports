from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='OCR for Reports',
    version='0.1',
    long_description=read('README.rst'),
    packages=['libs', 'reader', 'server'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pytesseract',
        'Flask',
        'flask-restful',
        'flasgger',
        'Pillow',
        'google-cloud-vision'
    ]
)