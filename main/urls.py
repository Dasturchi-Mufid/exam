from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('destination/',views.destination,name='destination'),
    path('hotel/',views.hotel,name='hotel'),
    path('blog/',views.blog,name='blog'),
    path('blog-detail/<int:id>',views.blog_detail,name='blog_detail'),
]
