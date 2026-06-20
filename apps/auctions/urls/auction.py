from django.urls import path

from apps.auctions.views import (AuctionListCreateView, AuctionDetailView, CompleteAuctionView, UploadAuctionImageView)

urlpatterns = [
    path("", AuctionListCreateView.as_view(), name="auction-list-create"),
    path("<int:pk>/", AuctionDetailView.as_view(), name="auction-detail"),
    path("<int:pk>/complete/", CompleteAuctionView.as_view(), name="auction-complete"),
    path("<int:auction_id>/images/", UploadAuctionImageView.as_view(), name="auction-image-upload",),
]
