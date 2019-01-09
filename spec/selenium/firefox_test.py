import unittest
import os
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

BaseURL = os.environ.get('BaseURL')

class Remix_Tests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = Firefox(executable_path='/usr/local/bin/geckodriver', options=options)

    def test_check_showcase_link(self):
        driver = self.driver
        driver.get("https://" + BaseURL)
        showcase = driver.find_element_by_link_text("Explore")
        showcase.click()

    def test_check_media_link(self):
        driver = self.driver
        driver.get("https://" + BaseURL)
        media = driver.find_element_by_link_text("Learn")
        media.click()

    def test_check_projects_link(self):
        driver = self.driver
        driver.get("https://" + BaseURL)
        projects = driver.find_element_by_link_text("Build")
        projects.click()

    def test_verify_media_corps(self):
        driver = self.driver
        driver.get("https://" + (BaseURL) + "/media-corps")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
