from rest_framework import generics

from apps.bids.models import Bid
from apps.bids.serializers import (BidDetailSerializer,)


class BidHistoryView( generics.ListAPIView):
    serializer_class = (BidDetailSerializer)

    def get_queryset(self):

        return (
            Bid.objects.filter(auction_id=self.kwargs[ "auction_id"]).select_related("bidder")
        )