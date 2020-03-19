from django.test import TestCase

# NOTE: all unit tests return an error saying a queryset is needed; lecture 16 says this is fine
class IngredientsListPageTest(TestCase):
	
	def test_ingredients_list_page_returns_correct_html(self):
		response = self.client.get('/ingredients_list_page')
		self.assertTemplateUsed(response, 'ingredients_list.html')


class IngredientsDetailPageTest(TestCase):

	def test_ingredients_detail_page_returns_correct_html(self):
		response = self.client.get('/ingredients_detail_page')
		self.assertTemplateUsed(response, 'ingredients_detail.html')
	

class IngredientsUpdateFormPageTest(TestCase):

	def test_ingredients_update_form_page_returns_correct_html(self):
		response = self.client.get('/ingredients_update_form_page')
		self.assertTemplateUsed(response, 'ingredients_update_form.html')


class IngredientsCreateFormPageTest(TestCase):

	def test_ingredients_create_form_page_returns_correct_html(self):
		response = self.client.get('/ingredients_create_form_page')
		self.assertTemplateUsed(response, 'ingredients_create_form.html')