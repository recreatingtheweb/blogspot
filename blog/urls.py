from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index'),
	path('topics/', views.topics, name='topics'),
    path('topics/<int:tid>/', views.topic, name='topic'),


]
