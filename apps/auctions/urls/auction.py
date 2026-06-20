from django.urls import path

from apps.auctions.views import (AuctionListCreateView, AuctionDetailView, CompleteAuctionView,)

urlpatterns = [
    path("", AuctionListCreateView.as_view(),),
    path("<int:pk>/", AuctionDetailView.as_view(),),
    path("<int:pk>/complete/",CompleteAuctionView.as_view(),),
]