import speech_recognition as sr
import os

def rename_file_from_voice_command(command):
    try:
        words = command.split(" ")
        old_name = words[1]
        new_name = words[3]
        
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except Exception as e:
        print(f"Error: {e}")
    
def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    print("Listening for command to rename a file...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        rename_file_from_voice_command(command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the command.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    listen_for_command()
