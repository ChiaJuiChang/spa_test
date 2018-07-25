from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    # ex: /polls/
    path('car/', views.get_api, name='get_api'),
]
