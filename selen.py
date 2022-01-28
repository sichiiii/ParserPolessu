import os

from selenium import webdriver
from selenium.webdriver.common.by import By

class Selen():
    def __init__(self) -> None:
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--disable-dev-sh-usage')
        self.option.add_argument('--disable-gpu')
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--headless')
        self.browser = webdriver.Chrome(executable_path=os.path.dirname(os.path.abspath(__file__)) + '/chromedriver', options=self.option)

    def get_screen(self, group_name, week_name):
        link = f'https://www.polessu.by/ruz/?q={group_name}'
        self.browser.get(link)
        self.browser.set_window_size(1000,1200)
        self.browser.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div/button').click()
        self.browser.find_element(By.XPATH, '//a[@href="#w' + str(int(week_name)-21) + '"]').click()
        self.browser.save_screenshot("my_screenshot.png")
        self.browser.quit()