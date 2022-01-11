from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions as selexcept
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
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
        #self.driver.implicitly_wait(5)
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
        time.sleep(6)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        time.sleep(2)

    def find_hashtag(self, hashtag):
        self.driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(1)

    def first_photo_by_hashtag(self):
        first = self.driver.find_element_by_class_name('_9AhH0')
        first.click()

    def like_photo(self):
        #like = self.driver.find_element_by_class_name('_8-yf5 ')
        #action = ActionChains(self.driver)
        #action.move_to_element(like).click().perform()
        #time.sleep(4)
        #like.click()
        #print(like.text)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "_8-yf5 "))).click()


        #self.driver.find_element_by_xpath('//*[@aria-label="Like"]')
        #try:
            #self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div/span/svg')
           # time.sleep(2)
       # except selexcept.NoSuchElementException:
           # self.driver.find_element_by_xpath('//*[@aria-label="Like"]').click()
          #  time.sleep(2)

    def close_driver(self):
        self.driver.close()
