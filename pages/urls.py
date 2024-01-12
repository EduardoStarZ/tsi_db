from django.urls import path
from pages import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', views.admin, name="admin"),
    path('search/', views.search, name='search'),
    path('admin_search/', views.admin_search, name='admin-search')
    ]
