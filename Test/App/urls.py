from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static,url

urlpatterns = [
    url(r'^list$', views.formation_list),
    path('detail_view/<int:pk>',views.Formation_DetailView.as_view(), name='detail'),
]