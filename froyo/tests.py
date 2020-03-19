from django.test import TestCase


class IngredientsListPageTest(TestCase):
	
	def test_ingredients_list_page_returns_correct_html(self):
		response = self.client.get('/ingredients_list_page')
		self.assertTemplateUsed(response, 'ingredients_list.html')
	# NOTE: returns error saying queryset is needed; lecture 16 says this is fine