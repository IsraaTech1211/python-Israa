import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)


def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Recognize voice input"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please speak clearly.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""


to_do_list = []


def set_reminder():
    """Set a reminder"""
    speak("What should I remind you about?")
    reminder = listen()
    if reminder:
        speak("In how many seconds should I remind you?")
        try:
            seconds = int(listen())
            speak(f"I will remind you in {seconds} seconds.")
            time.sleep(seconds)
            speak(f"Reminder: {reminder}")
        except ValueError:
            speak("Invalid time input.")


def add_to_do():
    """Add an item to the to-do list"""
    speak("What task should I add?")
    task = listen()
    if task:
        to_do_list.append(task)
        speak(f"Added {task} to your to-do list.")


def show_to_do():
    """Show the to-do list"""
    if to_do_list:
        speak("Here is your to-do list.")
        for task in to_do_list:
            speak(task)
    else:
        speak("Your to-do list is empty.")


def search_web():
    """Search the web using Google"""
    speak("What do you want to search for?")
    query = listen()
    if query:
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")


def main():
    """Main function to handle voice commands"""
    speak("Hello, I am Fifi, your assistant. How can I help you?")
    failure_count = 0

    while True:
        command = listen()

        if command == "":
            failure_count += 1
            if failure_count >= 3:
                speak("I'm having trouble understanding. Restarting.")
                break
            continue

        failure_count = 0

        if "reminder" in command:
            set_reminder()
        elif "add task" in command or "to-do" in command:
            add_to_do()
        elif "show tasks" in command or "to-do list" in command:
            show_to_do()
        elif "search" in command or "browse" in command or "google" in command:
            search_web()
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that. Please try again.")


if __name__ == "__main__":
    main()
