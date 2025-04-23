import cv2
import numpy as np
import pillow_heif
from PIL import Image
import os

color_dict = {
    'yellow': [np.array([25, 100, 100]),np.array([31, 255, 255])],
    'red': [np.array([0, 95, 0]), np.array([9, 255, 216])],
    'red': [np.array([170, 100, 70]), np.array([179, 255, 255])],    
    'green': [np.array([32, 98, 50]), np.array([84, 255, 255])],
    'turquoise': [np.array([84, 140, 50]), np.array([90, 255, 255])],
    'orange': [np.array([10, 100, 120]), np.array([25, 255, 255])],
    'blue': [np.array([91, 125, 50]), np.array([124, 255, 255])],
    'purple': [np.array([124, 170, 50]), np.array([138, 255, 255])],
    'brown': [np.array([14,61,0]),np.array([30, 180, 107])],
    'pink': [np.array([139, 121, 217]), np.array([169, 255, 255])],
    'grey': [np.array([0, 0, 40]), np.array([179, 25, 229])],
    'black': [np.array([0, 0, 0]), np.array([179, 255, 35])],
    'white': [np.array([0, 0, 230]), np.array([179, 23, 255])],
    
    
}

def convert_heic_to_jpg(heic_path):
    heif_file = pillow_heif.read_heif(heic_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw"
    )
    jpg_path = heic_path + ".jpg"
    image.save(jpg_path, "JPEG")
    return jpg_path


def color_dectector(img: str, color_dict:dict):
    temp_jpg = None
    
    # If HEIC, convert first
    if img.lower().endswith(".heic"):
        temp_jpg = convert_heic_to_jpg(img)
        img = temp_jpg

    
    img = cv2.imread(img)
    if img is None:
        raise ValueError("Image not found or invalid path provided.")
    

    blurred_img = cv2.GaussianBlur(img, (11, 11), 0)
    hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)
    #hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  old
    detected_colors = []
    for color_name, hsv_range in color_dict.items():
        #print('running')
        if hsv_range is not None:
            #print('passed')
            lower_hsv, upper_hsv = hsv_range
            mask = cv2.inRange(hsv_img,lower_hsv,upper_hsv)
            
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

            #print(np.count_nonzero(mask))
            if np.count_nonzero(mask) > 500:  # Threshold to reduce false positives
                print(f"Detected color: {color_name}")
                detected_colors.append(color_name)
        #print(50*'-')

    if temp_jpg and os.path.exists(temp_jpg):
        os.remove(temp_jpg)

    return detected_colors
        
        
print(color_dectector('IMG_2106.HEIC', color_dict))