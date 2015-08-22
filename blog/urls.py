# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:32:20 2015

@author: Nikolay_Semyachkin
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

