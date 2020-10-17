from django.urls import path

from . import views
from .views import *

urlpatterns=[
    path('',create_view, name='hrms'),
    path('list',list_view, name='hrms'),
    path('<id>/delete', delete_view,name='hrms'), 
    path('<id>/update', update_view,name='hrms'), 
    path('<id>/detail',detail_view, name='hrms'),
    ]