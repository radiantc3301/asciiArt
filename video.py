import cv2
from PIL import Image
import time
import os

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    aspect_ratio = image.shape[0] / image.shape[1]
    new_height = int(aspect_ratio * new_width * 0.55)
    return cv2.resize(image, (new_width, new_height))

def map_pixels_to_ascii(image):
    return ''.join([ASCII_CHARS[pixel//25] for pixel in image.flatten()])

def convert_frame_to_ascii(frame, new_width=100):
    frame = resize_image(frame, new_width)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ascii_str = map_pixels_to_ascii(frame)
    img_width = frame.shape[1]
    
    ascii_str_len = len(ascii_str)
    return "\n".join([ascii_str[index:(index+img_width)] for index in range(0, ascii_str_len, img_width)])

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def convert_video_to_ascii(video_path, new_width=100):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        ascii_frame = convert_frame_to_ascii(frame, new_width)
        clear_console()
        print(ascii_frame)
        time.sleep(0.2/fps)
    
    cap.release()

if __name__ == "__main__":
    video_path = 'bad_apple.mp4'
    convert_video_to_ascii(video_path)