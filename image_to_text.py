import cv2
import easyocr
import ssl
import os
import time
import json

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

# Create a directory for models if it doesn't exist
os.makedirs('.models', exist_ok=True)

# Set environment variable for model storage
os.environ['EASYOCR_MODULE_PATH'] = os.path.join(os.getcwd(), '.models')

# File to store the detected text
TEXT_FILE = 'detected_text.json'

def save_text(text):
    with open(TEXT_FILE, 'w') as f:
        json.dump({'text': text, 'timestamp': time.time()}, f)

try:
    # Initialize EasyOCR reader
    print("Initializing EasyOCR...")
    reader = easyocr.Reader(["en"], download_enabled=True)
    print("EasyOCR initialized successfully!")
except Exception as e:
    print(f"Error initializing EasyOCR: {e}")
    exit(1)

try:
    # Open the webcam (0 is the default camera)
    print("Opening camera...")
    cap = cv2.VideoCapture(0)
    
    # Try different camera indices if 0 doesn't work
    if not cap.isOpened():
        print("Trying alternative camera...")
        cap = cv2.VideoCapture(1)
    
    if not cap.isOpened():
        print("Error: Could not open webcam. Please check camera permissions.")
        print("On macOS, you may need to grant camera access to Terminal/Python.")
        exit(1)

    # Set the resolution
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Height

    print("Starting OCR... Press Ctrl+C to quit")
    print("----------------------------------------")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        try:
            # Perform OCR
            results = reader.readtext(gray)

            # Clear previous line
            print("\033[K", end="\r")
            
            # Process and save detected text
            if results:
                text = " ".join([result[1] for result in results])
                print(f"Detected text: {text}", end="\r")
                save_text(text)  # Save to file
            else:
                print("No text detected", end="\r")
                save_text("")  # Save empty string when no text detected
                
        except Exception as e:
            print(f"Error during OCR: {e}")
            continue

        # Small delay to prevent overwhelming the terminal
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopping...")
except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    # Release the webcam
    if 'cap' in locals():
        cap.release()
    print("\nCamera released")
