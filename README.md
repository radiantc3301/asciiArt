# asciiArt

an ascii art code that will get convert a picture to an ASCII art which consists of 10 ascii characters which arranged by the order of their intensity.

To make the ascii art pillow python library is used which can be installed by the command `pip install pillow` This library helps to convert the said image to a grayscale image of varying intensity from 0 to 255. 0 meaning total black and 255 meaning total white. Now based on this intensity ascii characters will be decided and implemented.

There are some cusrom images in directory which can be used to make the ascii art by simply changing the `image_path` variable to the required file path. Custom images can also converted to ascii art by adding that image in the directory. The ascii art will be outputed in the output.txt. In order to change the size of the art change the `new_width` variables present in the `resize_image()` function and `convert_image_to_ascii()` function. Please note that on increasing the `new_width` variable will increase the detail of the art but it will also increase its size.
