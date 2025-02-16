import os
from config import Config
from logger import Logger


def is_fontsize_ok() -> bool:
    custom_path = Config().general["local_prefs_path"]
    user_dir = os.path.expanduser("~")
    default_path = f"{user_dir}\\Documents\\Diablo IV/LocalPrefs.txt"
    file_path = custom_path if custom_path != "" else default_path
    if not os.path.exists(file_path):
        Logger.warning(
            "Could not find LocalPrefs.txt to check font size. Make sure you have font size set to small! If you have, ignore this warning."
        )
        return True
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            if 'FontScale "0"' not in file_content:
                return False
    except PermissionError:
        Logger.warning(
            "No premission to check the LocalPrefs.txt. Make sure you have font size set to small! If you have, ignore this warning."
        )
    return True
