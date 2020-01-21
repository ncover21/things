import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "things",
    version = "0.0.1",
    author = "Noah Cover",
    author_email = "ncover13@gmail.com",
    description = ("Command Line Based To Do List"),
    license = "BSD",
    keywords = "to do list command line",
    url = "https://github.com/ncover21/things",
    entry_points = {
        'console_scripts': ['things=things_app.things:main'],
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
    ],
)