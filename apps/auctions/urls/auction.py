from django.urls import path

from apps.auctions.views import (AuctionListCreateView, AuctionDetailView, CompleteAuctionView,)

urlpatterns = [
    path("", AuctionListCreateView.as_view(), name="auction-list-create"),
    path("<int:pk>/", AuctionDetailView.as_view(), name="auction-detail"),
    path("<int:pk>/complete/", CompleteAuctionView.as_view(), name="auction-complete"),
]
