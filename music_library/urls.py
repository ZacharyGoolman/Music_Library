from django.urls import path
from . import views
#  period means from the current folder
# url path ties into my view folder into the get @api request songs_list


urlpatterns = [
    path('', views.songs_list),
]