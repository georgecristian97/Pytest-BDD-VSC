import os, time
from selenium import webdriver

class APP:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self._driver = webdriver.Chrome(options=options)

    @property
    def driver(self):
        return self._driver

    def take_screenshot(self, text):
        self._driver.set_window_size(1368, 768)
        time.sleep(0.3)
        self._driver.get_screenshot_as_file(text+'-'+time.strftime("%Y%m%d_%H-%M-%S")+'.png')
        self._driver.maximize_window()
        #return full_path
