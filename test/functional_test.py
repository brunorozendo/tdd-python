import unittest

from selenium import webdriver


class ProjectRunning(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_is_server_running(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main()
