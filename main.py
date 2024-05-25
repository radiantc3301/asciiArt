from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=500):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width *0.4)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=25):
    pixels = list(image.getdata())
    ascii_str = ''.join([ASCII_CHARS[pixel//range_width] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=500):
    image = Image.open(image_path)
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index+img_width)] for index in range(0, ascii_str_len, img_width)])
    return ascii_img

def save_ascii_art(ascii_art, output_file):
    with open(output_file, 'w') as f:
        f.write(ascii_art)

if __name__ == "__main__":    
    image_path = '8.png'
    output_file = 'output.txt'
    
    ascii_art = convert_image_to_ascii(image_path)
    save_ascii_art(ascii_art, output_file)
    print("ASCII art saved to", output_file)
