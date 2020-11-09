from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'aboutus.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ProductsView(TemplateView):
    template_name = 'products.html'