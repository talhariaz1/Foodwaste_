"""
URL configuration for foodwaste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from education import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path("learning_activities/", views.learning_activities, name="learning_activities"),
    path("animals/", views.animals, name="animals"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("food_waste_list/", views.food_waste_list, name="food_waste_list"),
    path("food_waste/", views.food_waste_create, name="food_waste_create"),
    path(
        "food_waste/<int:pk>/update/", views.food_waste_update, name="food_waste_update"
    ),
    path(
        "food_waste/<int:pk>/delete/", views.food_waste_delete, name="food_waste_delete"
    ),
]
