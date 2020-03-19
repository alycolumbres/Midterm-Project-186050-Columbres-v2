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


class RecipesListPageTest(TestCase):
	
	def test_recipes_list_page_returns_correct_html(self):
		response = self.client.get('/recipes_list_page')
		self.assertTemplateUsed(response, 'recipes_list.html')


class RecipesDetailPageTest(TestCase):
	
	def test_recipes_detail_page_returns_correct_html(self):
		response = self.client.get('/recipes_detail_page')
		self.assertTemplateUsed(response, 'recipes_detail.html')


class RecipesUpdateFormPageTest(TestCase):

	def test_recipes_update_form_page_returns_correct_html(self):
		response = self.client.get('/recipes_update_form_page')
		self.assertTemplateUsed(response, 'recipes_update_form.html')


class RecipesCreateFormPageTest(TestCase):

	def test_recipes_create_form_page_returns_correct_html(self):
		response = self.client.get('/recipes_create_form_page')
		self.assertTemplateUsed(response, 'recipes_create_form.html')


class OrdersListPageTest(TestCase):
	
	def test_orders_list_page_returns_correct_html(self):
		response = self.client.get('/orders_list_page')
		self.assertTemplateUsed(response, 'orders_list.html')


class OrdersDetailPageTest(TestCase):
	
	def test_orders_detail_page_returns_correct_html(self):
		response = self.client.get('/orders_detail_page')
		self.assertTemplateUsed(response, 'orders_detail.html')


class OrdersUpdateFormPageTest(TestCase):

	def test_orders_update_form_page_returns_correct_html(self):
		response = self.client.get('/orders_update_form_page')
		self.assertTemplateUsed(response, 'orders_update_form.html')


class OrdersCreateFormPageTest(TestCase):

	def test_orders_create_form_page_returns_correct_html(self):
		response = self.client.get('/orders_create_form_page')
		self.assertTemplateUsed(response, 'orders_create_form.html')