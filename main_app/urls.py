from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='cats_index'),
  path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
]