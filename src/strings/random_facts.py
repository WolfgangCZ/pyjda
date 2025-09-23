"""
Fun facts with pyjda
"""

RANDOM_FACTS: list[str] = [
'''
Python runs your code using a program called an "interpreter".
Think of the interpreter like a chef who reads a recipe and cooks it step by step. 
Because of this, you usually don't need to compile the whole code (turn into machine code) before running it.
''',

'''
You can use Python in different styles:
- Write step-by-step instructions (procedural).
- Group data and behavior together (object-oriented).
- Use small functions that return values (functional).
This makes Python good for many kinds of projects.
''',

'''
CPython is the most common Python program and is written in the C language.
There are other versions too (for speed or to work with other platforms),
but they all let you write the same Python code in most cases.
''',

'''
Python comes with many useful tools already included. This is called the "Standard Library".
It has helpers for reading files, working with dates, talking to the internet, and more — so you 
often don't need to install extra packages for common tasks.
''',

'''
Python uses indentation (spaces at the start of a line) to show which lines belong together.
This makes Python code look neat and is one reason many beginners find it easier to read.
''',

'''
In Python you don't have to tell the computer the type of a variable (like number or text) before using it.
That makes writing code faster. If you want extra safety, you can add "type hints" to help both people 
and tools understand your code.
''',

'''
List comprehensions let you create lists in a short, readable way.
Generators let you create values one-by-one when needed, which saves memory if you have a lot of data.
''',

'''
There are thousands of extra packages you can install from the Python Package Index (PyPI) using "pip".
Use virtual environments (venv) to keep these packages separate for each project so they do not conflict.
''',

'''
You can do more than one thing at a time in Python:
- Threads let you run tasks that wait (like downloading files) in parallel.
- multiprocessing runs separate processes for CPU-heavy work.
- async/await is good for many small tasks that wait for I/O.
Be aware: in the common Python interpreter (CPython), threads have a Global Interpreter Lock (GIL) that affects some CPU-bound programs.
''',

'''
People use Python for many jobs: building websites, analyzing data, automating boring tasks, making scripts, and more.
It is popular because it is easy to read, has many libraries, and a big community to help you learn.
''',

'''
Python is beginner-friendly because you can run small experiments quickly.
Try opening a Python prompt and type: print("Hello, world!") — you will see the output immediately, which helps you learn fast.
''',

'''
Python files usually end with .py. To run a file named example.py, use: python example.py
This simple workflow makes trying code and sharing examples easy.
However you dont need to use .py in your file name to run it using Python.
''',

'''
Errors are normal when learning. Python gives readable error messages showing where the problem happened.
Use the message and the line number to find and fix mistakes step by step.
''',

'''
You can read and write files with only a few lines in Python.
For example: 
with open("notes.txt", "w") as f:
    f.write("Hello")
This makes Python great for small automation tasks.
''',

'''
Python has helpful online documentation and many tutorials.
If you get stuck, search for "Python <topic>" — you'll usually find examples and answers from the community.
'''
]
