from django.conf.urls import url

from .views import IngredientsListView, IngredientsDetailView, IngredientsUpdateFormView, IngredientsCreateFormView

urlpatterns = [
	url(r'^ingredients_list_page$', IngredientsListView.as_view(), name='Ingredients_List_View'),
	url(r'^ingredients_detail_page$', IngredientsDetailView.as_view(), name='Ingredients_Detail_View'),
	url(r'^ingredients_update_form_page$', IngredientsUpdateFormView.as_view(), name='Ingredients_Update_Form_View'),
	url(r'^ingredients_create_form_page$', IngredientsCreateFormView.as_view(), name='Ingredients_Create_Form_View'),
]