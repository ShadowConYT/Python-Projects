import pyautogui
import time
import speech_recognition as sr
from pygetwindow import getActiveWindow
from pywinauto import Desktop, findwindows


# Function to get the active input field
def get_active_input_field():
    try:
        active_window = getActiveWindow()
        app = Desktop(backend="uia").window(handle=active_window._hWnd)
        input_fields = app.descendants(control_type="Edit")
        return input_fields
    except findwindows.ElementNotFoundError:
        return None

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

while True:
    input_fields = get_active_input_field()

    if input_fields:
        print("Input fields found in the active window:")
        for field in input_fields:
            print("Control: ", field)
        
        text = speech_to_text()
        if text:
            pyautogui.typewrite(text) 

    time.sleep(1)