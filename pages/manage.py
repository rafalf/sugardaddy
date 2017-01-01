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


class Manage(Page, unittest.TestCase):

    def __init__(self, driver, conf, locators):
        self.driver = driver
        self.conf = conf
        self.locators = locators

    def select_basic_info(self):
        self.get_element_by_css('a[href="/manage/profile/edit_basic_info/"]').click()

    def select_location(self):
        self.get_element_by_css('a[href="/manage/profile/edit_location/"]').click()

    def enter_name(self, name):
        el = self.get_element_by_css('#name')
        el.clear()
        el.send_keys(name)

    @property
    def get_name(self):
        name = self.get_element_by_css('#name').get_attribute('value')
        return name

    def enter_headline(self, headline):
        el = self.get_element_by_css('#headline')
        el.clear()
        el.send_keys(headline)

    @property
    def get_headline(self):
        return self.get_element_by_css('#headline').get_attribute('value')

    def select_networth(self, value):
        select = Select(self.get_element_by_css(self.locators['net_worth']))
        select.select_by_value(str(value))

        selected = select.options[value].text
        return selected

    def get_networth(self):

        select = Select(self.get_element_by_css(self.locators['net_worth']))
        return select.first_selected_option.text

    def select_income(self, value):
        select = Select(self.get_element_by_css(self.locators['income']))
        select.select_by_value(str(value))

        selected = select.options[value].text
        return selected

    def get_income(self):
        select = Select(self.get_element_by_css(self.locators['income']))
        return select.first_selected_option.text

    def select_country(self, value):
        select = Select(self.get_element_by_css(self.locators['country']))
        select.select_by_value(str(value))

        selected = select.options[value - 1].text
        return selected

    def get_country(self):
        select = Select(self.get_element_by_css(self.locators['country']))
        return select.first_selected_option.text

    def select_city(self, value):
        select = Select(self.get_element_by_css(self.locators['city']))
        select.select_by_value(str(value))

        selected = select.options[value].text
        return selected

    def get_city(self):
        select = Select(self.get_element_by_css(self.locators['city']))
        return select.first_selected_option.text

    def select_bkk_area(self, value):
        select = Select(self.get_element_by_css(self.locators['bkk_area']))
        select.select_by_value(str(value))

        selected = select.options[value].text
        return selected

    def get_bkk_area(self):
        select = Select(self.get_element_by_css(self.locators['bkk_area']))
        return select.first_selected_option.text
