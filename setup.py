from setuptools import find_packages, setup
from reader import extract_text
from libs import hocr_search
setup(
    author="Senura Seneviratne",
    author_email="senuraa@msn.com",
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        "package": extract_text,
        "package": hocr_search
    }
)