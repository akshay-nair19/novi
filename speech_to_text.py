import os
import sys
import pyaudio
from vosk import Model, KaldiRecognizer
import json

MODEL_PATH = "vosk-model-en-us-0.22-lgraph"

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

print("Listening... Speak into the microphone.")

try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):  # If a complete sentence is recognized
            result = json.loads(recognizer.Result())  # Convert JSON output to dictionary
            text = result.get("text", "").strip()  # Extract recognized text
            if text:
                print("You said:", text)
except KeyboardInterrupt:
    print("\nStopping...")
    stream.stop_stream()
    stream.close()
    audio.terminate()
