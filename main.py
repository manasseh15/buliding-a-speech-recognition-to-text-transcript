import speech_recognition as sr
r=sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            print("Say Something")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print(f"recognizer text : {text}")
    except:
        print("you were trying to be funny")
        r = sr.Recognizer()
        continue        