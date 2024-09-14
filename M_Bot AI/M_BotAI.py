import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import time
import brain
import requests
from twilio.rest import Client


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class Assistant:
    def __init__(self):
        pass  # Initialize any attributes or methods here

    def speak(self, audio):
        print(audio)
        engine.say(audio)
        engine.runAndWait()

    def listen(self):
        """Listens for user input using speech recognition and returns the recognized text."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print("User said:", query)
            return query.lower()
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return ""

    def process_query(self, query):
        if 'wikipedia' in query:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            self.speak("According to Wikipedia")
            print(results)
            self.speak(results)
        elif 'open youtube' in query:
            self.speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        elif 'open whatsapp' in query:
            self.speak("Opening whatsapp...")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open google' in query:
            self.speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        elif 'play music' in query:
            self.speak("Playing music...")
            # Add your music playing functionality here
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"Sir, the time is {str_time}")
        elif 'send message' in query:
            try:
                self.speak("What should I say?")
                content = self.listen()
                account_sid = 'YourTwilioAccountSID'
                auth_token = 'YourTwilioAuthToken'
                sender_no = 'YourTwilioSenderNumber'
                receiver_no = 'ReceiverNumber'
                self.send_sms(content, sender_no, receiver_no, account_sid, auth_token)
                self.speak("Message has been sent!")
            except Exception as e:
                print(e)
                self.speak("I am not able to send this message")
        elif 'shutdown system' in query:
            try:
                self.speak("Are you sure you want to shut down? Say yes to confirm.")
                confirm = self.listen()
                if 'yes' in confirm:
                    self.speak("Shutting down the system...")
                    os.system("shutdown /s /t 1")
                else:
                    self.speak("Shutdown cancelled.")
            except Exception as e:
                print(e)
                self.speak("Error shutting down the system.")
        elif 'exit' in query:
            self.stop()

    def send_sms(self, body, sender, receiver, account_sid, auth_token):
        """Sends an SMS using the Twilio API."""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body,
            from_=sender,
            to=receiver
        )
        print("Message SID:", message.sid)

    def start(self):
        while True:
            query = self.listen()
            self.process_query(query)

    def stop(self):
        print("Exiting M_Bot AI. Goodbye!")
        exit()

def process_query(query):
    """Process user queries and take actions based on the query."""
    if 'open whatsapp' in query:
        speak("Opening WhatsApp...")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'in WhatsApp' in query:
        parts = query.split('in WhatsApp')
        if len(parts) > 1:
            action_part = parts[1].strip()
            if 'contact name is' in action_part and 'type' in action_part:
                contact_name = action_part.split('contact name is')[1].split('type')[0].strip()
                message = action_part.split('type')[1].strip()
                type_whatsapp_message(contact_name, message)
                return


def speak(text):
    """Speaks the provided text."""
    # Add your code for text-to-speech here
    
def type_whatsapp_message(contact_name, message):
    """Types a message in the specified WhatsApp chat."""
    try:
        # Activate WhatsApp window (assuming it's already open)
        pyautogui.click(x=100, y=100)  # Adjust the coordinates as needed
        time.sleep(1)  # Add a small delay to ensure WhatsApp is active
        
        # Search for the contact by typing their name
        pyautogui.write(contact_name)
        pyautogui.press("enter")
        time.sleep(1)  # Add a small delay to ensure the chat is opened
        
        # Type the message
        pyautogui.write(message)
        pyautogui.press("enter")
        
        speak("Message sent successfully!")
    except Exception as e:
        print(e)
        speak("Failed to send the message.")

if __name__ == "__main__":
    # Example usage:
    type_whatsapp_message("idiot", "hello")

def wishMe(assistant):
    """Greets the user based on the time of the day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        assistant.speak("Good Morning!")
    elif 12 <= hour < 18:
        assistant.speak("Good Afternoon!")
    else:
        assistant.speak("Good Evening!")
    assistant.speak("I am your Assistant. How can I help you?")

if __name__ == '__main__':
    assistant = Assistant()
    wishMe(assistant)
    assistant.start()
