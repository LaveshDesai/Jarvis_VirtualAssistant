import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import sys


r = sr.Recognizer()
newsapi = "pub_58409bd310b054fd40cec2cdca7cf86cf4ecd"

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if(c.lower() == "open google"):
        webbrowser.open("https://google.com")

    elif(c.lower() == "open youtube"):
        webbrowser.open("https://youtube.com")

    elif(c.lower() == "open hotstar"):
        webbrowser.open("https://hotstar.com")

    elif(c.lower() == "open netflix"):
        webbrowser.open("https://netflix.com")
    
    elif(c.lower() == "open chat"):
        webbrowser.open("https://chatgpt.com")
   
    elif(c.lower() == "open jio"):
        webbrowser.open("https://jiocinema.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsdata.io/api/1/latest?apikey=pub_58409bd310b054fd40cec2cdca7cf86cf4ecd")
        if r.status_code == 200:
            data = r.json()  # Parse the JSON response
            articles = data.get('results', [])  # Get the 'results' which contains the articles

        # Loop through the articles and print the details
        for article in articles:
            title = article.get('title', 'No title')
            speak(title)

  
    elif c.lower() == "stop jarvis":
        speak("Stopping now. Goodbye!")
        # Exits the loop and stops the program
        sys.exit()
    
    

if(__name__ == "__main__"):
    speak("Initializing Jarvis...")

    #Listen for the wake word Jarvis
    while True:
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source,timeout=5,phrase_time_limit=10)
            word = r.recognize_google(audio)
            print(word)
            if (word.lower() =="jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
           
            
        except sr.WaitTimeoutError:
            print("Error: Listening timed out. Please try speaking again.")

        except sr.UnknownValueError:
            print("Error: Could not understand the audio.")

        except sr.RequestError as e:
            print(f"Error: Could not request results from Google Speech Recognition service; {e}")
