from sys import platform
from time import sleep

import keyboard
import speech_recognition as sr

if platform == "win32":
    from winsound import Beep
else:
    import os

    def Beep(freq, duration):
        os.system(f'play -nq -t alsa synth {duration} sine {freq}')

# Run code below to check available Microphone
"""
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with name '{name}' found for `Microphone(device_index={index})`")
"""

while True:
    sleep(0.5)
    if keyboard.is_pressed('PAUSE'):
        mic = sr.Microphone(device_index=1)
        r = sr.Recognizer()
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)
                Beep(300, 500)
                audio = r.listen(source)
                keyboard.write(r.recognize_google(audio, language="ru-RU").capitalize())
                Beep(300, 500)
            except sr.UnknownValueError as e:
                pass

