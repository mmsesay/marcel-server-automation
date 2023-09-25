"""
Filename        :   marcel.py
Description     :   This file has a class with methods to that automates processes into Marcel's server
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   25.09.2023
Completed on    :   in progress
"""

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from ..secrets import secrets


class MarcelServer:
    def __init__(self):
        self.options = Options()

        # bypass for non-secure page in chrome
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')

        # headless mode makes the Chrome browser hidden when running the script.
        # Uncomment the following line at anytime to show the browser
        self.options.add_argument('headless')

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        time.sleep(5)
        # driver. get('chrome://settings/clearBrowserData')

        self.driver.get("https://162.0.236.72:2087/")

    def __login_input_elements(self):
        """
        This method finds the email and password input elements and fill in.
        It then finds the login button element and click on it to navigate to the next page
        """

        print("finding the elements")

        # wait until the email element is located
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='user']")))
        email_field.send_keys(secrets['MARCEL_SERVER_USER'])  # input the value into the form field
        time.sleep(2)

        # wait until the password element is located
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='pass']")))
        password.send_keys(secrets['MARCEL_SERVER_PASS'])  # input the value into the form field
        time.sleep(2)

        # find the buttons on the page
        login_button = self.driver.find_elements(By.XPATH, "//button[@name='login']")
        login_button[0].click()
        time.sleep(2)
        print("Login Successful")
        # print("next button clicked")

    def login(self):
        """
        This method finds all the elements required to logged successfully into twitter
        """

        try:
            self.__login_input_elements()
            print("Redirected Successfully to the dashboard")
        except NoSuchElementException:
            print("One or more elements weren't found!!!")
        except TimeoutException:
            print("Timeout error!!!")
