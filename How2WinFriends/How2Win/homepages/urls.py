from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import lessonPageView


urlpatterns = [ 
path('', indexPageView, name='index'),
path('about/', aboutPageView, name='about'),
path('lessons/', lessonPageView, name='lesson')
] 

