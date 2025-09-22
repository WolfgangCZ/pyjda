import os
from dataclasses import dataclass
from enum import Enum

@dataclass
class Folders:
    LECTURES = "lectures"
    ORIGINALS = "originals"
    SOLUTIONS = "solutions"

@dataclass
class Chapters:
    C01_PRINT = "01_print"
    C02_VARIABLES = "02_variables"

class Lessons:
    L01_HELLO_WORLD = "01_hello_world.py"
    L02_PRINT = "02_print.py"


CHAPTER_1_DIR = os.path.join(Folders.LECTURES, Chapters.C01_PRINT)

class LessonsEnums(Enum):
    C01_L01_HELLO_WORLD = 1
    C01_L02_PRINT = 2

class LessonsPaths:
    L01_HELLO_WORLD_PATH = os.path.join(CHAPTER_1_DIR, Lessons.L01_HELLO_WORLD)
    L02_PRINT_PATH = os.path.join(CHAPTER_1_DIR, Lessons.L02_PRINT)
