from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('<int:user_id>/results/', views.results, name='results'),
    # path('<int:user_id>/vote/', views.vote, name='vote'),
]