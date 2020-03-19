from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView


class IngredientsListView(ListView):
	model = None


class IngredientsDetailView(DetailView):
	model = None


class IngredientsUpdateFormView(UpdateView):
	model = None
	template_name_suffix = '_update_form'


class IngredientsCreateFormView(CreateView):
	model = None
	template_name_suffix = '_create_form'


class RecipesListView(ListView):
	model = None


class RecipesDetailView(DetailView):
	model = None


class RecipesUpdateFormView(UpdateView):
	model = None
	template_name_suffix = '_update_form'


class RecipesCreateFormView(CreateView):
	model = None
	template_name_suffix = '_create_form'


class OrdersListView(ListView):
	model = None


class OrdersDetailView(DetailView):
	model = None


class OrdersUpdateFormView(UpdateView):
	model = None
	template_name_suffix = '_update_form'


class OrdersCreateFormView(CreateView):
	model = None
	template_name_suffix = '_create_form'