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


class Home(Page, unittest.TestCase):

    def __init__(self, driver, conf, locators):
        self.driver = driver
        self.conf = conf
        self.locators = locators

    def wait_page_loaded(self):
        selector_css= self.locators.get('signup_name')
        self._wait_page_loaded(selector_css)

    def enter_name(self, name):
        selector_css = self.locators.get('signup_name')
        self.get_element_by_css(selector_css).send_keys(name)

    def enter_email(self, email):
        self.get_element_by_css('#email').send_keys(email)

    def enter_password(self, password):
        self.get_element_by_css('#password').send_keys(password)

    def enter_confirm_password(self, password):
        self.get_element_by_css('#confirm_password').send_keys(password)

    def select_sugar_daddy(self):
        self.get_element_by_css('input[value="1"]').click()

    def select_men(self):
        self.get_element_by_css('[name="men"]').click()

    def select_agree(self):
        self.get_element_by_css('[name="agree"]').click()

    def select_submit(self):
        self.get_element_by_css('[type="submit"]').click()

    def select_date_of_birth(self, month='January', day='1', year='1979'):
        select = Select(self.get_element_by_css('#month'))
        select.select_by_visible_text(month)
        select = Select(self.get_element_by_css('#day'))
        select.select_by_visible_text(day)
        select = Select(self.get_element_by_css('#year'))
        select.select_by_visible_text(year)

    def select_gender(self, gender='Male'):
        select = Select(self.get_element_by_css('#gender'))
        select.select_by_visible_text(gender)