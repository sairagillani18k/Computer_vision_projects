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
we studied the basics operation that are very important for our cv journy and we also make simple project from it.
<br/>
***what we learn:***
- Read and Write image
- Read and Write video
- Apply that we make reverse from any given video <br/>
![reverse video](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/opencv/reversed_video.gif)

- Draw the shapes on the image: its helpful in detection and loclaization task

![line_and_figures](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/opencv/line_and_figure.png)

![polygon](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/opencv/poloygon.png)
<br/>
- Image rotation and translation

### Applying Filters 
#### Computer vision Terminology 
- **Image filter:** The kernel is called the image filter.
- **Image filtering:** The process of applying  kernel to given image is called image filtering
- **Filtered image:** The output image after applying the kernel to the image is called the filtered image <br/>
      
![kernel](https://github.com/sairagillani18k/Computer_vision_projects/blob/main/custom_filtering/kernel_img.png)

#### What is frequency in image
- Frequency refers to the **rate of change of pixel values**.
- Sharp edges would be **High frequency** because pixel values change rapdily.
- Plain areas would be **Low frequency** because pixel values not change to much.

#### High pass filters 
- High pass filter is the type of frequency domain filter that **attenuates the low frequency** and preserves the high frequency componnents.

#### Low pass filters 
- Low pass filter is the type of frequency domain filter that **attenuates the high frequency** and preserves the low frequency componnents.

 ##### Application
- Bluring the image [***click here***](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/bluring_denoising)<br/>
![bluring](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/bluring_denoising/blur.jpg)
- Sharpning the image [***click here***](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/sharpning)<br/>
![sharpning](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/sharpning/sharpned.jpg)
- Denoising the image [***click here***](https://github.com/sairagillani18k/Computer_vision_projects/tree/main/bluring_denoising)<br/>
![denoising]((https://github.com/sairagillani18k/Computer_vision_projects/tree/main/bluring_denoising/denoise.jpg)



