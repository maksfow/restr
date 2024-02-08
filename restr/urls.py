from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('search',views.search_restaurant),
    path('about',views.about,name='about'),
    path('kuxnya',views.kuxnya,name='kuxnya'),
    path('kuxnya/<int:pk>',views.kuxnyaa,name='kuxnyaa'),
    path('zavedeniye',views.zavedeniye,name='zavedeniye'),
    path('zavedeniye/<int:pk>',views.zavedeniyee,name='zavedeniyee'),
    path('restaurant/<int:pk>',views.restaurantt),
    path('menu',views.menu,name='menu'),
    path('menu/<int:pk>',views.menuu,name='menuu'),
    path('review',views.review,name='review'),
    path('review/<int:pk>',views.revieww,name='revieww'),
    path('not-found',views.not_found),
    path('register', views.Register.as_view()),
    path('createrev',views.createrev),
    path('book',views.book),




]