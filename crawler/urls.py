# -*- coding: utf-8 -*-
"""
@author: ryanou97
"""

from django.urls import path, include
from crawler import views

urlpatterns = [
    path('',views.simple_crawl),    
    path('POST_crawl/',views.POST_crawl),
]