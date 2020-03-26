#!/usr/bin/env python3
# coding:utf-8
"""
@Author : Lucky Jason
@Email  : LuckyJasonone@gmail.com
@Description : urls.py
@Starting time : 2020/3/26
@Completion time : null
"""
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
