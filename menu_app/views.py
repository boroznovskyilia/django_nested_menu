from django.shortcuts import render
from .models import MenuItem
from django.views.generic import TemplateView,ListView

class MenuView(TemplateView):
    template_name='menu_app/details.html'

class StartMenuView(TemplateView):
    template_name='menu_app/home.html'