# Computer_vision
## Image basics
### what is image??
Image is describe as a 2-D function f(x,y) where (x,y)
are the spatial coordinates and the value of f at any point (x,y)
is proportional to the brightness or gray levels of the image.
<br/> x -> [0,h-1], where h is the height of the image
<br/> y -> [0,w-1], where w is the width of the image
<br/> f(x,y) -> [0,L-1] where L = 256 (for an 8-bit image)
<br/>
![image](https://sites.google.com/a/online.sch.im/computing-at-snhs/_/rsrc/1437054062818/curriculum/computer-science/theory/3-year-7-graphic-processing/binary-images-1/8bytes.png?height=154&width=320)
### Image vs Digital image.
The value of f(x,y) will always be a discrete value in digital image but in image may or may not.

## Numpy basics for Computer Vision :  [*click here*](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/Numpy_for_cv/)


NumPy is the fundamental package for scientific computing in Python.
Its play arround arrays as we know image is also representable in form of arrays.
we play with image using Numpy we also create masks, and filters etc by numpy we aslo create image in this Exercise using numpy fuction that we studied.

## Opencv : [*click here*](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/opencv/)
**OpenCV** provides a real-time optimized Computer Vision library, tools, and hardware.
we studied the basics operation that are very importan for our cv journy and we also make simple project from it.
<br/>
***what we learn:***
- Read and Write image
- Read and Write video
- Apply that we make reverse from any given video <br/>
![reverse video](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/opencv/reversed_video.gif)
<br/>
- Draw the shapes on the image: its helpful in detection and loclaization task
<br/>
![shape_1](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/opencv/line_and_figure.png)
<br/>
![shape_1](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/opencv/poloygon_figure.py)
