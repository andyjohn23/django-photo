from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<category>/', views.CategoryListView.as_view(), name="category"),
    path('search/', views.image_search, name='image-search'),
]