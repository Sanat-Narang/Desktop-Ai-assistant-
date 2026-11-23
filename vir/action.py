import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather


def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual Assistant")
        return "My name is virtual Assistant"

    elif "hello" in user_data or "hye" in user_data or "hay" in user_data:
        text_to_speech.text_to_speech("Hey sir, How can I help you!")
        return "Hey sir, How can I help you!"

    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I am doing great these days sir")
        return "I am doing great these days sir"

    elif "thanku" in user_data or "thank" in user_data:
        text_to_speech.text_to_speech("It's my pleasure sir to stay with you")
        return "It's my pleasure sir to stay with you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning sir, I think you might need some help")
        return "Good morning sir, I think you might need some help"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data or "quit" in user_data:
        text_to_speech.text_to_speech("Ok sir")
        return "Ok sir"

    elif "play music" in user_data or "song" in user_data:
        text_to_speech.text_to_speech("gaana.com is now ready for you, enjoy your music")
        webbrowser.open("https://gaana.com")
        return "gaana.com is now ready for you, enjoy your music"

    elif "open google" in user_data or "google" in user_data:
        text_to_speech.text_to_speech("Google open")
        url = 'https://google.com/'
        webbrowser.get().open(url)
        return "Google open"

    elif "youtube" in user_data or "open youtube" in user_data:
        text_to_speech.text_to_speech("YouTube open")
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        return "YouTube open"
    elif "open facebook" in user_data or "facebook" in user_data:
        text_to_speech.text_to_speech("Facebook open")
        url = 'https://facebook.com/'
        webbrowser.get().open(url)
        return "Facebook open"

    elif "open instagram" in user_data or "instagram" in user_data:
        text_to_speech.text_to_speech("Instagram open")
        url = 'https://instagram.com/'
        webbrowser.get().open(url)
        return "Instagram open"

    elif "what time is it"  in user_data or "current time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "weather" in user_data or "temperature" in user_data:
        temp = weather.weather()
        text_to_speech.text_to_speech(temp)
        return temp
    elif "what's up" in user_data or "whats up" in user_data:
        text_to_speech.text_to_speech("I am doing great these days sir")
        return "I am doing great these days sir"
    elif "ok" in user_data or "ok sir" in user_data:
        text_to_speech.text_to_speech("Ok sir")
        return "Ok sir"
    elif "good night" in user_data:
        text_to_speech.text_to_speech("Good night sir, have a good sleep")
        return "Good night sir, have a good sleep"
    


    else:
        text_to_speech.text_to_speech("Sorry, I did not understand that.")
        return "Sorry, I did not understand that."
