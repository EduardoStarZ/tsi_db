from django.urls import path
from pages import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', views.admin, name="admin")
    ]
