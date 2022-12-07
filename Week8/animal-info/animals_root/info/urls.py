
from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.get_animal, name='animal'),
    path('', views.animal_info, name='animal'),
    path('', views.get_family, name='family'),
    path('', views.family_info, name='family'),
]
# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route