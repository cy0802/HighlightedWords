# Highlighted Words
## Introduction
This is a tool that aims to translate the highlighted English words in a picture.
Currently, we assume all the highlighters are yellow, and hand-writing words are not accepted.
## Usage
### Clone the repository
```
git clone https://github.com/cy0802/HighlightedWords.git
```
### Install Python
Go to [the download page](https://www.python.org/downloads/) and select a version to download. (latest version often has some problem)

Remember to click `add to Path` while installing.
### Install all the packages
In this project, we use `flask`, `bs4`, `requests`, `opencv-python`, and `pytesseract`.

To install them, you can simply use the package installer for Python, pip.

Type this in your command line. Replace {packageName} for the package you want to install.
```
pip install {packageName}
```

### Install Pytesseract
(this is for windows os)

For the package that performs OCR, we need some extra step to complete the installation.

Please follow this [instruction](http://python-learnnotebook.blogspot.com/2020/01/pytesseract.html).

After installation, you should modify the `pytesseract.pytesseract.tesseract_cmd` variable in `imgToStr.py` to the path where you install the tesseract package.

### flask run
type this in your command line, 
```
flask run
```
and a development server will be started.

If you want a picture to try, there is an image in `./static/upload/`.

## The Website
Originally we deployed it on Heroku. However, Heroku terminated its free service in 2022, so we don't have a website now.