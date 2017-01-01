#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page import Page


class Messages(Page, unittest.TestCase):

    def __init__(self, driver, conf, locators):
        self.driver = driver
        self.conf = conf
        self.locators = locators

    def wait_page_loaded(self):
        self._wait_page_loaded('.panel-profile')

    def select_user(self):
        self.get_element_by_css('a[href^="/manage/date/view/?user_id"]').click()
        # wait for message body
        self.wait_for_element_by_css('#body')

    def enter_message(self, message):
        self.get_element_by_css('#body').send_keys(message)

    def get_all_messages(self):
        els = self.driver.find_elements_by_css_selector('.media-body>p')
        return [el.text for el in els]

