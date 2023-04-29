# Fancybbox
[![PyPi version](https://img.shields.io/pypi/v/fancybbox)](https://pypi.org/project/fancybbox/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A package that allows to build Lib is a package that enables users to create visually appealing bounding boxes for object detection in image processing deep learning projects.  
With a current version of 0.0.10, the package is constantly being updated and improved. The package offers a variety of features, including the ability to customize the appearance of bounding boxes with different colors, line widths, and styles. 
Additionally, it provides users with the flexibility to adjust the size and shape of the bounding boxes to meet their specific needs.'


Developed by Prashant Verma (c) 2023

This project still very much experimental and may change significantly. 

## Install
Install with all dependencies:

```bash
pip install fancybbox
```

## Examples of How To Use (Alpha Version)

Creating A Sample detection function

```python
import cv2
from fancy_bbox import FancyBox

# Load an image
image = cv2.imread("images/img_1.jpg")

# Detect an object and get its bounding box coordinates
x, y, w, h = [100, 100, 200, 200]

# Create a FancyBox object and draw it on the image
fancy_box = FancyBox(x, y, w, h, border_thickness=1, border_color=(0, 255, 0))
image_with_box = fancy_box.target_angle_bbox(image)


# Display the image with the box
cv2.imshow("Fancy Box Example", image_with_box)
cv2.waitKey(0)
```

