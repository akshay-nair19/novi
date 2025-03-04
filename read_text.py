import json
import time
from gtts import gTTS
import os
import pygame
import tempfile
import cv2
import easyocr
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

def speak_text(text):
    if not text or text == "No text file found" or text == "Error reading text file":
        return
        
    try:
        # Create a temporary file for the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_filename = fp.name
            
        # Generate speech
        tts = gTTS(text=text, lang='en')
        tts.save(temp_filename)
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load and play the audio
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # Clean up
        pygame.mixer.quit()
        os.unlink(temp_filename)
        
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def main():
    try:
        # Initialize EasyOCR reader
        print("Initializing EasyOCR...")
        reader = easyocr.Reader(["en"], download_enabled=True)
        print("EasyOCR initialized successfully!")
    except Exception as e:
        print(f"Error initializing EasyOCR: {e}")
        return

    try:
        # Open the webcam
        print("Opening camera...")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Trying alternative camera...")
            cap = cv2.VideoCapture(1)
        
        if not cap.isOpened():
            print("Error: Could not open webcam. Please check camera permissions.")
            return

        # Set the resolution
        cap.set(3, 640)  # Width
        cap.set(4, 480)  # Height

        print("Starting OCR and Text-to-Speech... Press Ctrl+C to quit")
        print("----------------------------------------")

        last_text = ""  # Keep track of last spoken text

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

                # Process detected text
                if results:
                    text = " ".join([result[1] for result in results])
                    print(f"\rDetected text: {text}", end="")
                    
                    # Only speak if the text is different from last time
                    if text and text != last_text:
                        print(f"\nSpeaking: {text}")
                        speak_text(text)
                        last_text = text
                else:
                    print("\rNo text detected", end="")
                    
            except Exception as e:
                print(f"\nError during OCR: {e}")
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

if __name__ == "__main__":
    main() 