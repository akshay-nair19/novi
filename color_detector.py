import cv2
import numpy as np

# img = cv2.imread('image.jpg')

#exp for yellow

color_dict = {
    'yellow': [np.array([20, 100, 100]),np.array([30, 255, 255])],
    'red': [np.array([155, 25, 0]), np.array([179, 255, 255])],
    'green': [np.array([30, 50, 50]), np.array([85, 255, 255])],
    'orange': [np.array([5, 100, 100]), np.array([15, 255, 255])],
    'blue': [np.array([90, 50, 50]), np.array([130, 255, 255])],
    'violet': [np.array([115, 50, 50]), np.array([160, 255, 255])],
    'brown': [np.array([16,100,1]),np.array([19, 255, 255])],
    'pink': [np.array([160, 100, 100]), np.array([179, 255, 255])],
}

def color_dectector(img: str, color_dict:dict):
    img = cv2.imread(img)
    if img is None:
        raise ValueError("Image not found or invalid path provided.")
    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    detected_colors = []
    for color_name, hsv_range in color_dict.items():
        # print('running')
        if hsv_range is not None:
            # print('passed')
            lower_hsv, upper_hsv = hsv_range
            mask = cv2.inRange(hsv_img,lower_hsv,upper_hsv)
            
            if np.count_nonzero(mask) > 50:  # Threshold to reduce false positives
                # print(f"Detected color: {color_name}")
                detected_colors.append(color_name)
        # print(50*'-')
    return detected_colors
        
        
# print(color_dectector('Orange-braun.png', color_dict))

