import time
from selenium import webdriver


class Web(object):
    def __init__(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)

    def open(self, url):
        self.browser.get(url)

    def click(self, xpath):
        self.browser.find_element_by_xpath(xpath).click()

    def read(self, xpath):
        self.browser.find_element_by_xpath(xpath).text

    def write(self, xpath, text):
        self.browser.find_element_by_xpath(xpath).send_keys(text)
