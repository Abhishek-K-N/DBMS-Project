from django.urls import path
from . import views
urlpatterns=[
    path("cardata/", views.car_data, name="cardata"),
    path("", views.login)
]