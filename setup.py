from setuptools import setup, find_packages

setup(
    name='HighlightedWords',
    version='1.0.0',
    url='https://github.com/cy0802/HighlightedWords.git',
    author='cy0802',
    description='an application that translate the highlighted words in a picture',
    packages=find_packages(),    
    install_requires=[
        'flask',
        'gunicorn',
        'opencv-python-headless',
        'bs4',
        'pytesseract',
        'requests',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'HighlightedWords=app:app',
        ],
    },
)