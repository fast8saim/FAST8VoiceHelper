import speech_recognition
import subprocess

sr = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

if query == 'привет джарвис':
    print('Привет, Саймон')
elif query == 'как дела':
    print('Норм, сам как?')
elif query == 'открой калькулятор':
    subprocess.Popen('calc.exe')
else:
    print('Не понял, повтори')