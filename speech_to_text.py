import os
import sys
import pyaudio
from vosk import Model, KaldiRecognizer
import json
import threading
import queue

MODEL_PATH = "vosk-model-en-us-0.42-gigaspeech"
WAKE_WORD = "novi"
CHUNK_SIZE = 1024

if not os.path.exists(MODEL_PATH):
    print("Please download the Vosk model!")
    sys.exit(1)

# Loading the Vosk model
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=CHUNK_SIZE)
stream.start_stream()

# Create a queue for audio data
audio_queue = queue.Queue()
is_running = True

def audio_callback():
    while is_running:
        try:
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
            audio_queue.put(data)
        except Exception as e:
            print(f"Error reading audio: {e}")
            break

# Start audio thread
audio_thread = threading.Thread(target=audio_callback)
audio_thread.start()

print("Waiting for wake word 'Novi'...")

try:
    while True:
        try:
            data = audio_queue.get(timeout=0.1)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip().lower()
                
                if text:
                    if WAKE_WORD in text:
                        print("\nWake word detected! Listening...")
                        # Start listening for command
                        command_recognizer = KaldiRecognizer(model, 16000)
                        
                        while True:
                            try:
                                command_data = audio_queue.get(timeout=0.1)
                                if command_recognizer.AcceptWaveform(command_data):
                                    command_result = json.loads(command_recognizer.Result())
                                    command_text = command_result.get("text", "").strip()
                                    
                                    if command_text:
                                        print("\rYou said: " + command_text, end="", flush=True)
                                        
                                        # Check for stop command
                                        if "stop" in command_text.lower():
                                            print("\nStopping listening...")
                                            break
                            except queue.Empty:
                                continue
                            except Exception as e:
                                print(f"\nError processing command: {e}")
                                break
        except queue.Empty:
            continue
        except Exception as e:
            print(f"\nError in main loop: {e}")
            break

except KeyboardInterrupt:
    print("\nStopping...")
    is_running = False
    audio_thread.join()
    stream.stop_stream()
    stream.close()
    audio.terminate()
