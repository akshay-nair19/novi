import os
import sys
import pyaudio
from vosk import Model, KaldiRecognizer
import json

MODEL_PATH = "vosk-model-en-us-0.42-gigaspeech"
WAKE_WORD = "novi"

if not os.path.exists(MODEL_PATH):
    print("Please download the Vosk model!")
    sys.exit(1)

# Loading the Vosk model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
stream.start_stream()

print("Waiting for wake word 'Novi'...")

try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").strip().lower()
            
            if text:
                if WAKE_WORD in text:
                    print("\nWake word detected! Listening...")
                    # Start listening for command
                    command_recognizer = KaldiRecognizer(model, 16000)
                    
                    while True:
                        command_data = stream.read(4096, exception_on_overflow=False)
                        if command_recognizer.AcceptWaveform(command_data):
                            command_result = json.loads(command_recognizer.Result())
                            command_text = command_result.get("text", "").strip()
                            
                            if command_text:
                                print("You said:", command_text)
                
except KeyboardInterrupt:
    print("\nStopping...")
    stream.stop_stream()
    stream.close()
    audio.terminate()