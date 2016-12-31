from . import reader
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os


def get_driver():

    browser = reader.get_conf().get('browser', 'Chrome')
    cwd = os.path.dirname(__file__)

    if browser == 'Firefox':
        binary = FirefoxBinary(os.path.join(cwd, 'drivers', 'firefox.exe'))
        driver = webdriver.Firefox(firefox_binary=binary)
    elif browser == 'Chrome':
        driver = webdriver.Chrome(os.path.join(cwd, 'drivers', 'chromedriver.exe'))
    elif browser == 'Chrome-OSX':
        driver = webdriver.Chrome()
    elif browser == 'Ie':
        driver = webdriver.Ie(executable_path=os.path.join(cwd, 'drivers', 'IEDriverServer.exe'))
    elif browser == 'Safari':
        driver = webdriver.Safari()
    return driver
