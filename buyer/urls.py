from django.urls import path
from . import views

urlpatterns=[
    path('', views.buy,  name='buy'),
    path('view_more/<str:id>/', views.view_more, name='view_more')
]