from django.urls import path

from apps.bids.views import ( CreateBidView, BidHistoryView,)

urlpatterns = [
    path("<int:auction_id>/bids/", CreateBidView.as_view(),),
    path( "<int:auction_id>/bids/history/", BidHistoryView.as_view(),),
]