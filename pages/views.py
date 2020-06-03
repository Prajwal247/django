# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'
