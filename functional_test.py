import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	# employee opens website and sees the title
	#def test_can_open_website(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('The Good Place FroYo Shop', self.browser.title)

	# employee opens ingredients list page and checks title
	#def test_can_open_ingredients_list_page(self):
	#	self.browser.get('http://localhost:8000/ingredients_list_page')
	#	self.assertIn('Ingredients - List', self.browser.title)
	#	self.assertEqual(
	#		'http://localhost:8000/ingredients_list_page',
	#		self.browser.getCurrentUrl()
	#	)
	# NOTE: unit testing this returns an error because a queryset is not implemented

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')