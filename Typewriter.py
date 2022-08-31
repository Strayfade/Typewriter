# Module Imports
import cv2
import json
import time
import numpy
import random
import pyautogui
import pytesseract
import pyscreenshot

# Configuration
Config = None
with open("config.json") as ConfigFile:
   Config = json.load(ConfigFile) # Imports json config file for later use

LowercaseLetters=[]
for i in range(97,123):
    LowercaseLetters.append(chr(i)) # Generates an array of all default lowercase characters

cap = pyscreenshot.grab(bbox=(473, 139, 1428, 427)) # Capture screen area contaning letters, may need to be customized
tesstr = pytesseract.image_to_string(cv2.cvtColor(numpy.array(cap), cv2.COLOR_BGR2GRAY), lang="eng") # Run Tesseract character recognition on image
tesstr = tesstr.replace("\n", " ") # Remove newlines from scanned image output
tesstr = tesstr.replace("  ", " ") # Remove double-spacing artifact thingy

print(tesstr) # Lets us see what we're typing, useful for debugging

time.sleep(1) # Gives us a delay before the actual typing starts

for x in tesstr:
    LPM = Config["TargetWPM"] * 4.5 * 20 # Get letters per minute multiplied by average letters in word (~4.5) multiplied by adjustment
    LPS = 1000 / (LPM / 60) / 1000 # Convert letters per minute into delay between each letter
    time.sleep(LPS * random.uniform(0.5, 5)) # Sleep with additional randomness
    ShouldMakeMistake = random.random() > Config["TargetAccuracy"] / 100 # Use TargetAccuracy to determine whether or not we should miss a letter
    if ShouldMakeMistake:
        Mistake = random.choice(LowercaseLetters) # Select a letter (hopefully incorrect) from array of all letters
        pyautogui.press(Mistake) # Press incorrect letter
        time.sleep(Config["MistakeReactionTime"]) # Wait for us to "notice" we made a mistake
        pyautogui.press("backspace") # Press backspace to remove incorrect letter
        time.sleep(LPS) # Sleep before next letter
    if x.isupper():
        pyautogui.keyDown("shift") # Hold shift if letter is uppercase
    pyautogui.press(x) # Send key
    if x.isupper():
        pyautogui.keyUp("shift") # Release shift if needed