import pyautogui
import speech_recognition as sr
import time



def open_google():
        pyautogui.hotkey("alt", "tab")
        pyautogui.hotkey('ctrl', 'n')
        pyautogui.write('www.google.com')
        pyautogui.press('enter')


    
def open_spotify():
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('spotify')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

def play_music():
    time.sleep(5)
    pyautogui.hotkey("space")

def close_current_window():
    pyautogui.hotkey("alt", "f4")
    
def take_screenshot():
    pyautogui.screenshot("yourscreenshot.png")

def search_up(query):
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey("alt", "tab")
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)
    pyautogui.write('https://www.google.com/search?q=' + query)
    pyautogui.press('enter')


 
 


commands = ["open google", "open spotify", "play music", "close the current window", "take a screenshot", "Search up", "open spotify and play music"]

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything:")
    audio = r.listen(source)

    try:
        global text
        text = r.recognize_google(audio)
        print("Your Text:",text)
        if text.lower() in commands:
            if text.lower() == "open google":
                open_google()
            elif text.lower() == "open spotify":
                open_spotify()
            elif text == "play_music":
                play_music()
            elif text == "close the current window":
                close_current_window()
            elif text == "take a screenshot":
                take_screenshot()
            elif "search" in text.lower():
                search_query = text.replace('search', '').strip()
                search_up(search_query)
            elif text.lower() == "open spotify and play music":
                open_spotify()
                play_music()
                
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



