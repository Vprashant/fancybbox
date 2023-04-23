from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.10'
DESCRIPTION = 'Fancy Bounding Box - Rectangle for Object Detection'
LONG_DESCRIPTION = 'A package that allows to build Lib is a package that enables users to create visually appealing bounding boxes for object detection in image processing deep learning projects.  \
                        With a current version of 0.0.10, the package is constantly being updated and improved. The package offers a variety of features, including the ability to customize the appearance of bounding boxes with different colors, line widths, and styles. \
                         Additionally, it provides users with the flexibility to adjust the size and shape of the bounding boxes to meet their specific needs.'

# Setting up
setup(
    name="fancybbox",
    version=VERSION,
    author="Prashant27050 (Prashant Verma)",
    author_email="prashant27050@gmail.com",
    description=DESCRIPTION,
    long_description= LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python'],
    keywords=['python', 'image processing', 'bbox', 'bbox regtangle', 'fancy rectangle', 'bounding box'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)