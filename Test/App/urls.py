from django.urls import path
from . import views

urlpatterns = [
    path('formations/', views.Formation_ListView.as_view()),

]