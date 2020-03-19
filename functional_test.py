import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	# initial testing
	def test_can_open_browser(self):
		self.browser.get('http://localhost:8000')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')