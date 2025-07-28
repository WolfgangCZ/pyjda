# import sys
import os
import time
from src import config

TARGET_FILE_PATH = config.LESSON_FILE
last_time = os.path.time(TARGET_FILE_PATH)

while True:
    current_time = os.path.time(TARGET_FILE_PATH)
    if last_time != current_time:
        last_time = current_time
        print(f"The file {TARGET_FILE_PATH} has been changed")
    time.sleep(1000)
