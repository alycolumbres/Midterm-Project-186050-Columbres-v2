from django.conf.urls import url

from .views import IngredientsListView, IngredientsDetailView, IngredientsUpdateFormView, IngredientsCreateFormView, RecipesListView, RecipesDetailView, RecipesUpdateFormView, RecipesCreateFormView, OrdersListView, OrdersDetailView, OrdersUpdateFormView, OrdersCreateFormView

urlpatterns = [
	url(r'^ingredients_list_page$', IngredientsListView.as_view(), name='Ingredients_List_View'),
	url(r'^ingredients_detail_page$', IngredientsDetailView.as_view(), name='Ingredients_Detail_View'),
	url(r'^ingredients_update_form_page$', IngredientsUpdateFormView.as_view(), name='Ingredients_Update_Form_View'),
	url(r'^ingredients_create_form_page$', IngredientsCreateFormView.as_view(), name='Ingredients_Create_Form_View'),

	url(r'^recipes_list_page$', RecipesListView.as_view(), name='Recipes_List_View'),
	url(r'^recipes_detail_page$', RecipesDetailView.as_view(), name='Recipes_Detail_View'),
	url(r'^recipes_update_form_page$', RecipesUpdateFormView.as_view(), name='Recipes_Update_Form_View'),
	url(r'^recipes_create_form_page$', RecipesCreateFormView.as_view(), name='Recipes_Create_Form_View'),
	
	url(r'^orders_list_page$', OrdersListView.as_view(), name='Orders_List_View'),
	url(r'^orders_detail_page$', OrdersDetailView.as_view(), name='Orders_Detail_View'),
	url(r'^orders_update_form_page$', OrdersUpdateFormView.as_view(), name='Orders_Update_Form_View'),
	url(r'^orders_create_form_page$', OrdersCreateFormView.as_view(), name='Orders_Create_Form_View')
]