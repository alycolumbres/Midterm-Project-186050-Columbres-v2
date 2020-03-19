from django.conf.urls import url

from .views import IngredientsListView

urlpatterns = [
	url(r'^ingredients_list_page$', IngredientsListView.as_view(), name='Ingredients_List_View'),
]