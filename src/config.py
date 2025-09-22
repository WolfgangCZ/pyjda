import os
from src.constants import Folders
from xml.etree import ElementTree as ET

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(THIS_DIR, os.pardir)

LECTURES_FOLDER = os.path.join(ROOT, Folders.LECTURES)
ORIGINALS_FOLDER = os.path.join(ROOT, Folders.ORIGINALS)
USER_CONFIG_PATH = os.path.join(ROOT, "config.xml")

class UserConfig:
    def __init__(self, root: ET.Element):
        self._root = root

    @property
    def first_run(self):
        pass

    def get_lesson_info(self, chapter_name: str, lesson_name: str):
        pass

_user_config: UserConfig | None = None

def get_user_config() -> UserConfig:
    global _user_config
    if _user_config is not None:
        return _user_config
    _user_config = UserConfig(ET.parse(USER_CONFIG_PATH).getroot())
    return _user_config
