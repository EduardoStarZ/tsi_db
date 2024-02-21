from django.urls import path
from models import views

urlpatterns = [
        path('search/', views.search),
        path('admin_search/', views.admin_search)
]
