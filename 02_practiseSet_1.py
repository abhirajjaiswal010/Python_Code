
#? que-1 -> write the program to print twinkle twinkle little start poem in python

print('''
      Song Lyrics
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.
      ''')

#? que-2 -> install an external module and use it to perform an operation of your interest 

import pyttsx3
engine = pyttsx3.init()
engine.say("hi abhiraj ")
engine.runAndWait()

#? ques-3 -> write a python program to print the content of a directory using the os module . 

# list_directory.py
import os

# get current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# list all files and folders
print("\nContents of directory:")
for item in os.listdir(current_dir):
    print(item)
