from django.urls import path
from .views import ShopView, ShopdetailViews, CardView, Card

urlpatterns = [
    path("", ShopView.as_view(), name="shop"),
    path("<int:pk>", ShopdetailViews.as_view(), name='shopdetail'),
    path("", CardView.as_view(), name="card")
]