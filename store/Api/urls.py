from django.urls import path
from .views import ListClothes,DetailView,AddToCartView


urlpatterns=[
    path('clothes/',ListClothes.as_view(),name='clothes'),
    path('details/<int:pk>/',DetailView.as_view(),name='details'),
    path('add-to-cart/',AddToCartView.as_view(),name='add-to-cart'),
]