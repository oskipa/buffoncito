from django.urls import path
from . import views

app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('comment/', views.comment, name='comment'),
    path('<slug:category>/<int:year>/<int:month>/<int:day>/<slug:title>.aspx', views.article, name='article'),
]
