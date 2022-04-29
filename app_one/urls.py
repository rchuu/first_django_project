from django.urls import path
# the . indicates that the views file can be found in the same directory as this file
from . import views

urlpatterns = [
    path('', views.index),
    # would only match localhost:8000/bears
    path('bears', views.one_method),
    # would match localhost:8000/bears/23
    path('bears/<int:my_val>', views.another_method),
    # would match localhost:8000/bears/pooh/poke
    path('bears/<str:name>/poke', views.yet_another),
    # would match localhost:8000/17/brown
    path('<int:id>/<str:color>', views.one_more),
]
# This is the same url function, but this time our arguments indicate that:
# '' - the rest of the route both starts and ends with nothing (i.e. "/" is the full route), and
# views.index - if the requested route matches this pattern, then the function with the name "index" from this app's views.py file will be invoked.
