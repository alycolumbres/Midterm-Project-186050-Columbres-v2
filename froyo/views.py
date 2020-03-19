from django.shortcuts import render

from django.views.generic.list import ListView

class IngredientsListView(ListView):
	model = None