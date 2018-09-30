# ReadDiabetesReports

An attempt at extracting values from diabetes report using tessarct and google vision
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

*   Python3 [https://www.python.org/downloads/]
*   Tesseract [https://github.com/tesseract-ocr/tesseract/wiki]
*   Google cloud vision, service account [https://cloud.google.com/vision/]


### Installing

1.  Install dependencies with the requirements.txt. Use the below command at the project root to install dependencies.

```
pip install -r requirements.tt
```

2. Add google service account JSON file to the path.

For Linux/MacOS

```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

For Windows (With powershell)

```
$env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

3. Start the python application.

Run:

```
   python3 pyserver.py
```

4. Open http://localhost:5001/apidocs in your browser to the see the API documentation.


## Authors

* **Senura Seneviratne** - *Initial work*

See also the list of [contributors](https://github.com/senuraa/ReadDiabetesReports/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
