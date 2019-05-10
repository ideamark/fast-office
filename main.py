from selenium import webdriver
from lib.word import Word
from lib.excel import Excel
from lib.web import Web
from lib.common import *

Firefox = webdriver.Firefox(executable_path=r'./drivers/geckodriver.exe')
Chrome = webdriver.Chrome(executable_path=r'./drivers/chromedriver.exe')
