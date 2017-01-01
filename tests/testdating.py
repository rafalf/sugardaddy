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

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from utils import reader
from utils import browser

from pages.home import Home
from pages.manage import Manage
from pages.login import Login
from pages.messages import Messages


class TestDating(unittest.TestCase):

    def setUp(self):

        self.conf = reader.get_conf()
        self.locators = reader.get_locators()

        self.driver = browser.get_driver()

        self.driver.get(self.conf.get('site_url'))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_1_signup(self):

        home = Home(self.driver, self.conf, self.locators)

        home.wait_page_loaded()

        # sign up
        home.enter_name(home.random_word)

        home.enter_email('{}{}@upwork.com'.format(home.random_word, home.random_number))

        home.enter_password('password01')

        home.enter_confirm_password('password01')

        home.select_date_of_birth()

        home.select_gender()

        home.select_sugar_daddy()

        home.select_men()

        home.select_agree()

        home.select_submit()

        manage = Manage(self.driver, self.conf, self.locators)

        # signed up
        manage.wait_for_nav_bar()

        manage.select_profile()

        manage.select_logout()

        # logged out - home page
        home.wait_page_loaded()

    def test_2_basic_info(self):

        login = Login(self.driver, self.conf, self.locators)

        self.driver.get(self.conf.get('site_login_url'))

        login.wait_page_loaded()

        login.enter_email(self.conf['user_man'])

        login.enter_password(self.conf['pass'])

        login.select_submit()

        manage = Manage(self.driver, self.conf, self.locators)

        # logged in
        manage.wait_for_nav_bar()

        manage.select_profile()

        manage.select_basic_info()

        random_name = manage.random_word
        manage.enter_name(random_name)

        random_headline = manage.random_word
        manage.enter_headline(random_headline)

        random_net = manage.random_value
        sel_net = manage.select_networth(random_net)

        random_income = manage.random_value
        sel_income = manage.select_income(random_income)

        # Save
        manage.select_submit(True)

        selected_net = manage.get_networth()

        selected_income = manage.get_income()

        # verify all values saved
        self.assertEqual(selected_net, sel_net)

        self.assertEqual(selected_income, sel_income)

        self.assertEqual(manage.get_name, random_name)

        self.assertEqual(manage.get_headline, random_headline)

        # verify on profile page
        manage.select_profile()

        profile_info = manage.get_info()

        income_text = "Annual Iconme: {}".format(sel_income)
        self.assertIn(income_text, profile_info)

        networth_text = "Net Worth: {}".format(sel_net)
        self.assertIn(networth_text, profile_info)

        manage.select_logout()

    def test_3_location(self):

        login = Login(self.driver, self.conf, self.locators)

        self.driver.get(self.conf.get('site_login_url'))

        login.wait_page_loaded()

        login.enter_email(self.conf['user_man'])

        login.enter_password(self.conf['pass'])

        login.select_submit()

        manage = Manage(self.driver, self.conf, self.locators)

        # logged in
        manage.wait_for_nav_bar()

        manage.select_profile()

        manage.select_location()

        random_country = manage.random_value
        sel_country = manage.select_country(random_country)

        # BKK
        manage.select_city(1)

        random_area = manage.random_value
        sel_area = manage.select_bkk_area(random_area)

        # Save
        manage.select_submit(True)

        selected_country = manage.get_country()

        selected_city = manage.get_city()

        selected_area = manage.get_bkk_area()

        # verify all values saved
        self.assertEqual(sel_country, selected_country)

        self.assertEqual('Bangkok', selected_city)

        self.assertEqual(sel_area, selected_area)

    def test_4_bio(self):

        login = Login(self.driver, self.conf, self.locators)

        self.driver.get(self.conf.get('site_login_url'))

        login.wait_page_loaded()

        login.enter_email(self.conf['user_man'])

        login.enter_password(self.conf['pass'])

        login.select_submit()

        manage = Manage(self.driver, self.conf, self.locators)

        # logged in
        manage.wait_for_nav_bar()

        manage.select_profile()

        manage.select_bio()

        manage.select_looking_for_men()

        random_lifestyle = manage.random_value
        sel_lifestyle = manage.select_lifestyle(random_lifestyle)

        manage.select_submit(True, True)

        manage.select_profile()

        profile_info = manage.get_info()

        self.assertIn('Lifestyle: {}'.format(sel_lifestyle), profile_info)

        self.assertIn('Age: 17 (Male)', profile_info)

    def test_5_messages(self):

        login = Login(self.driver, self.conf, self.locators)

        self.driver.get(self.conf.get('site_login_url'))

        login.wait_page_loaded()

        login.enter_email(self.conf['user_man'])

        login.enter_password(self.conf['pass'])

        login.select_submit()

        manage = Manage(self.driver, self.conf, self.locators)

        # logged in
        manage.wait_for_nav_bar()

        manage.select_messages()

        messages = Messages(self.driver, self.conf, self.locators)

        messages.wait_page_loaded()

        messages.select_user()

        random_message_man = messages.random_word
        messages.enter_message(random_message_man)

        messages.select_submit(True)

        messages.select_logout()

        # woman receives message
        self.driver.get(self.conf.get('site_login_url'))

        login.wait_page_loaded()

        login.enter_email(self.conf['user_woman'])

        login.enter_password(self.conf['pass'])

        login.select_submit()

        manage.wait_for_nav_bar()

        manage.select_messages()

        messages.select_user()

        messages_received = messages.get_all_messages()

        self.assertIn(random_message_man, messages_received)

        random_message_woman = messages.random_word
        messages.enter_message(random_message_woman)

        messages.select_submit(True)

        messages.select_logout()

        # man receives message
        self.driver.get(self.conf.get('site_login_url'))

        login.enter_email(self.conf['user_man'])

        login.enter_password(self.conf['pass'])

        login.select_submit()

        manage.wait_for_nav_bar()

        manage.select_messages()

        messages.wait_page_loaded()

        messages.select_user()

        messages_received = messages.get_all_messages()

        self.assertIn(random_message_woman, messages_received)


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(TestDating("test_1_signup"))
    suite.addTest(TestDating("test_2_basic_info"))
    suite.addTest(TestDating("test_3_location"))
    suite.addTest(TestDating("test_4_bio"))
    suite.addTest(TestDating("test_5_messages"))
    runner = unittest.TextTestRunner()
    runner.run(suite)