from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup as bs
import requests
import time


class Instagram:

    def __init__(self, env):
        self.username = env.get('username')
        self.password = env.get('password')
        self.url = env.get('url')

        self.soup = None

        self.options = webdriver.   ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=r'C:\_CHROMEDRIVER\bin\chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep(1)
        self.driver.get('chrome://settings/clearBrowserData')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//settings-ui').send_keys(Keys.ENTER)

    def open_browser(self):
        time.sleep(1)
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        #self.driver.maximize_window()
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

    def get_soup_object(self, hashtag):
        r = requests.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        self.soup = bs(r.content, 'html.parser')

    def first_photo_by_hashtag(self):
        time.sleep(1)
        first = self.driver.find_element(By.CLASS_NAME, '_9AhH0')
        first.click()

    def like_photo(self):
        time.sleep(4)
        like_button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
        print(like_button.text)
        # time.sleep(1)
        # like_button.click()

        # time.sleep(2)
        # srce = self.driver.find_element(By.XPATH, '//*[local-name()="svg"  and @aria-label="Like"]')
        # print(srce.text)
        # if srce == 'Like':
            # print('element pronađem')
        # else:
            # print('element nije pronađen')
        # div = self.soup.find('button', {'class': 'wpO6b  '})
        # svg = div.find('svg')
        # print(svg)
        # svg = like_button.get_attribute("svg aria-label")
        # print(svg)

        # try:
        # self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div/span/svg')
        # time.sleep(2)
        # except selexcept.NoSuchElementException:
        # self.driver.find_element_by_xpath('//*[@aria-label="Like"]').click()
        # time.sleep(2)

    def close_driver(self):
        self.driver.close()
