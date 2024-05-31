from screenshotSN.screenshot import take_screenshot
from screenshotSN.analyse import analyse_image

if __name__ == '__main__':
    take_screenshot()
    content = analyse_image("screenshots/screenshot.png")
    print(content)

