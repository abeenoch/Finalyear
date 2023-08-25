import openai
import asyncio
import pyttsx3
import pyaudio
import wave
import speech_recognition as sr

openai.api_key = "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"  # Replace with your actual API key

WAKE_UP_WORD = "assistant"  # Change this to your preferred wake-up word

def send_message(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

async def process_user_input(user_input, messages):
    messages.append({"role": "user", "content": user_input})
    response = await loop.run_in_executor(None, send_message, messages)
    print("Robot:", response)
    speak(response)
    messages.append({"role": "assistant", "content": response})

audio = pyaudio.PyAudio()
messages = []

loop = asyncio.get_event_loop()

def listen_for_wake_word():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    print("Listening for wake-up word...")
    frames = []
    
    for _ in range(0, int(RATE / CHUNK * 5)):  # Record for 5 seconds
        data = stream.read(CHUNK)
        frames.append(data)
    
    stream.stop_stream()
    stream.close()
    
    try:
        with wave.open("wakeup.wav", "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b"".join(frames))
        
        recognizer = sr.Recognizer()
        with sr.AudioFile("wakeup.wav") as source:
            audio_data = recognizer.record(source)
            spoken_text = recognizer.recognize_google(audio_data).lower()
            
            print("Spoken:", spoken_text)
            if WAKE_UP_WORD in spoken_text:
                return True
            return False

    except sr.UnknownValueError:
        return False
    except sr.RequestError:
        return False

async def main():
    while True:
        if listen_for_wake_word():
            print("Wake-up word detected.")
            speak("Hey, I'm your assistant. What can I do for you today?")
            while True:
                CHUNK = 1024
                FORMAT = pyaudio.paInt16
                CHANNELS = 1
                RATE = 16000
                
                stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
                
                print("Say something...")
                frames = []
                
                for _ in range(0, int(RATE / CHUNK * 5)):  # Record for 5 seconds
                    data = stream.read(CHUNK)
                    frames.append(data)
                
                stream.stop_stream()
                stream.close()
                
                try:
                    with wave.open("user_input.wav", "wb") as wf:
                        wf.setnchannels(CHANNELS)
                        wf.setsampwidth(audio.get_sample_size(FORMAT))
                        wf.setframerate(RATE)
                        wf.writeframes(b"".join(frames))
                    
                    recognizer = sr.Recognizer()
                    with sr.AudioFile("user_input.wav") as source:
                        audio_data = recognizer.record(source)
                        user_input = recognizer.recognize_google(audio_data)
                        print("You:", user_input)
                        await process_user_input(user_input, messages)

                except sr.UnknownValueError:
                    print("Sorry, could not understand your audio.")
                except sr.RequestError:
                    print("Could not request results; check your network connection.")

if __name__ == "__main__":
    loop.run_until_complete(main())
