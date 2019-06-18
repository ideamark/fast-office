import time
from selenium import webdriver


class Web(object):
    def __init__(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)

    def open(self, url):
        try:
            self.browser.get(url)
            return True
        except Exception:
            return False

    def click(self, xpath):
        try:
            self.browser.find_element_by_xpath(xpath).click()
            return True
        except Exception:
            return False

    def read(self, xpath):
        return self.browser.find_element_by_xpath(xpath).text

    def write(self, xpath, text):
        try:
            self.browser.find_element_by_xpath(xpath).send_keys(text)
            return True
        except Exception:
            return False

    def html(self):
        return self.browser.page_source
