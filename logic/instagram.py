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

        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_browser(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[text()='Accept All']").click()
        time.sleep(2)

        return self.driver

    def enter_credentials(self):
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@name ="username"]'))).send_keys(self.username)
        time.sleep(2)
        input_pass = self.driver.find_element_by_xpath('//*[@name ="password"]')
        input_pass.click()
        time.sleep(2)
        input_pass.send_keys(self.password)
        time.sleep(2)
        button = self.driver.find_element_by_xpath('//button[@type=\"submit\"]')  # todo ("//div[contains(text(), 'Log In')]")
        button.click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        time.sleep(2)

    def find_hashtag(self, hashtag):
        self.driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(2)
