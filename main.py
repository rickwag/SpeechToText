import speech_recognition as sr

recognizer = sr.Recognizer()
recognition_duration = 5

def start_talking():
    print("start talking")
    with sr.Microphone() as source:
        # read audio data from the default microphone
        audio_data = recognizer.record(source, duration=recognition_duration)
        print("Recognizing...")

        try:
            # convert speech to text
            text = recognizer.recognize_google(audio_data)
            print(text)
        except:
            print("sorry, something went wrong")

print("------speech to text------")
while True:
    print("\n---menu---")
    print("{0} Exit \n{1} Start Speech Recognizer \n{2} Change Recognition Duration")
    choice = int(input("enter corresponding number: "))

    match choice:
        case 0:
            break
        case 1:
            start_talking()
        case 2:
            try:
                recognition_duration = int(input("enter duration(in seconds): "))
            except TypeError:
                print("only integers allowed")