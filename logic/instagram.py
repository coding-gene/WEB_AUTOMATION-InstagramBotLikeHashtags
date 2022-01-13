from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions as selexcept
import time


class Instagram:

    def __init__(self, env):
        self.username = env.get('username')
        self.password = env.get('password')
        self.url = env.get('url')

        self.options = webdriver.   ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            chrome_options=self.options,
            executable_path=r'C:\_CHROMEDRIVER\bin\chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep(1)
        self.driver.get('chrome://settings/clearBrowserData')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//settings-ui').send_keys(Keys.ENTER)

    def open_browser(self):
        time.sleep(1)
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Accept All']").click()
        return self.driver

    def enter_credentials(self):
        time.sleep(2)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@name ="username"]'))).send_keys(self.username)
        time.sleep(2)
        input_pass = self.driver.find_element(By.XPATH, '//*[@name ="password"]')
        input_pass.click()
        time.sleep(2)
        input_pass.send_keys(self.password)
        time.sleep(2)
        button = self.driver.find_element(By.XPATH, '//button[@type=\"submit\"]')
        button.click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//button[text()='Not Now']").click()

    def find_hashtag(self, hashtag):
        time.sleep(2)
        self.driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

    def first_photo_by_hashtag(self):
        time.sleep(1)
        first = self.driver.find_element(By.CLASS_NAME, '_9AhH0')
        first.click()

    def like_first_photo(self):
        time.sleep(4)
        try:
            self.driver.find_element(By.XPATH,
                    '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]')
            like_button = self.driver.find_element(By.XPATH,
                    '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            like_button.click()
            time.sleep(2)
            next_button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/button')
            time.sleep(1)
            next_button.click()
        except selexcept.NoSuchElementException:
            print('Photo already liked!')
            pass

    def like_next_photo(self):
        time.sleep(4)
        try:
            self.driver.find_element(By.XPATH,
                    '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]')
            like_button = self.driver.find_element(By.XPATH,
                    '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            like_button.click()
        except selexcept.NoSuchElementException:
            print('Photo already liked!')
            pass

    def next_photo(self):
        time.sleep(2)
        nex = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]/button')
        return nex

    def continue_liking(self, number_of_photos_to_be_liked):
        for n in range(number_of_photos_to_like):
            n = self.next_photo()
            if n:
                self.like_next_photo()
                time.sleep(1)
                self.next_photo().click()
            else:
                print('Session ended!')
                break

    def close_last_photo(self):
        time.sleep(2)
        close = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/button')
        time.sleep(1)
        close.click()

    def close_driver(self):
        self.driver.close()
