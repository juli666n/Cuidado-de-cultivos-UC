from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url('updateCards', views.update_cards, name='update_cards'),
]
