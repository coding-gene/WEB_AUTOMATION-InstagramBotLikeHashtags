from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class Instagram:

    def __init__(self, env):
        self.username = env.get('username')
        self.password = env.get('password')
        self.url = env.get('url')
        self.hashtag = env.get('hashtag')
        self.hashtags = env.get('hashtags')

    def open_browser(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(5)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='Accept All']").click()
        time.sleep(2)

        return driver

    def test(self):
        pass
