from selenium import webdriver
import unittest

class ProjectRunning(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='~/geckodriver')

    def tearDown(self):
        self.browser.quit()

    def test_is_server_running(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
    unittest.Main()
