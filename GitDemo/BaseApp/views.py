from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):

    template_name = 'BaseApp/index.html'


class AnotherView(TemplateView):

    template_name = 'BaseApp/another.html'


class ThirdView(TemplateView):

    template_name = 'BaseApp/third.html'