import subprocess
import sys
import os
import io
from contextlib import redirect_stdout
from xml.etree import ElementTree as ET

from src import config
from src.constants import LessonsPaths
from src import strings

def check_edit():
    pass
        
def annoucment(text: str) -> None:
    print(text)
    print("===================")
    input("Press any key to continue")

def run_first_start(first_start: bool):
    if first_start:
        annoucment(strings.FIRST_WELCOME_01)
        clear_terminal()
        annoucment(strings.FIRST_WELCOME_02)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    should_exit = False
    first_start = True
    clear_terminal()
    run_first_start(first_start)

    while not should_exit:
        annoucment(strings.L01_HELLO_WORLD)
        user_input = input("Press enter to continue")
        

def check_first_lecture():

    output = subprocess.run(args=[sys.executable, LessonsPaths.L01_HELLO_WORLD_PATH], capture_output=True)
    all_prints = output.stdout.decode('utf-8').strip().split("\r\n")
    if len(all_prints) > 1:
        print("There is too many prints, isnt it? I wanted just one, so delete the rest please.")
        for i, pr in enumerate(all_prints):
            print(f"{i+1}. {pr}")
    elif len(all_prints) == 0:
        print("I dont see any print statements, did you write one?")
    else:
        hello_world_str = all_prints[0]
        cleaned_str = hello_world_str.strip("!., ").lower()
        if cleaned_str == "hello world":
            print("Congrats, you did it!")
        elif "hello" in cleaned_str and "world" in cleaned_str:
            print("I was expecting just 'Hello world!', but i guess good enough...")
        else:
            print(f"Uhm, I expected 'Hello world!' and not '{hello_world_str}'? Are you trolling me?")
