from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category>/<int:year>/<int:month>/<int:day>/<slug:title>.aspx', views.article, name='article'),
]
