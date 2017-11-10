## Exercise 1

*Question: How does a program read the cvMat object, in particular, what is the order of the pixel structure?*

Answer: A program would first index the height/rows and cols/width fields of the cvMat object to get the pixel data for the required location. The pixel structure will then vary based on the color scheme used, but usually would be accessed as a 3-value BGR struct.

## Exercise 2

*Question 1: ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.*

Answer: To view results, run color_image.py, ex.

    python color_image.py some_image.png

The Red, Green, and Blue images show the components of the image in the RGB spectrum as "grayscale" pictures, using the respective color instead of gray.

Th Y, Cr, Cb show the values of each picture in the YCrCb spectrum. Y, being the alpha component, shows up as a grayscale version of the original image. Cb and Cr, being blue- and red-differences, show a gradient of their values over the image.

Hue, Saturation, and Value correspond to the HSV spectrum. Value is greyscale due to it being the "alpha" of the image. Hue and Saturation, essentially being cylindrical coordinates in the H-S space, don't give an accurate representation of the image.

*Question 2: Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?*

Answer: For the test image baboon.png, the values are:

    | Color Space | Pixel Value     | Value ranges            |
    | ----------- | --------------- | ----------------------- |
    | RGB         | (102, 165, 156) | (0-255, 0-255, 0-255)   |
    | YCrCb       | (155, 129, 98)  | (0-255, 16-240, 16-240) |
    | HSV         | (34, 97, 165)   | (0-179, 0-255, 0-255)   |


## Exercise 3

*Question 1:  Look at the code in Noise.cpp and implement the code in Python. Also, print the results for different noise values in the Gaussian case, mean = 0, 5, 10, 20 and sigma = 0, 20, 50, 100 and for the salt-and-pepper case, pa = 0.01, 0.03, 0.05, 0.4 and pb = 0.01, 0.03, 0.05, 0.4.*

*Question 2: Change the kernel sizes for all the filters with all different values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work ”better” for images with salt-and-pepper noise and gaussian noise?*

Answer: To view the results, run:

    python noise.py some_image.png

This will output all of the different variations listed above for both questions.
Note that this is around 74 images altogether.

The higher the kernal size, the less efficient the filters seemed to perform. Interestingly, the
median filter worked best on both types of noise (Gaussian and salt-and-pepper), which is the only
filter that does not use a kernal size, just all adjacent pixels.
