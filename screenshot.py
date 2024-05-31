import logging
import pyautogui
from datetime import datetime

def take_screenshot():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    path = f"screenshots/screenshot.png"
    screenshot.save(path)
    logging.info(f"Took a screenshot, saved at {path}")
    return path

if __name__ == "__main__":
    take_screenshot()
