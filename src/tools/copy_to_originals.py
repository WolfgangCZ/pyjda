"""
Copy all folders and files from lectures to originals
"""

import shutil
import os

from src import config


def copy_to_originals():
    if os.path.exists(config.LECTURES_FOLDER):
        shutil.rmtree(config.LECTURES_FOLDER)
    shutil.copytree(config.ORIGINALS_FOLDER, config.LECTURES_FOLDER)

    print(f"Successfully copied {config.ORIGINALS_FOLDER} to {config.LECTURES_FOLDER}")

if __name__ == "__main__":
    confirm = input("Are you sure? Type 'yes' to continue: ")
    if confirm != "yes":
        print("Aborted")
        exit()
    copy_to_originals()