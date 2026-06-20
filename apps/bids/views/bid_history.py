from rest_framework import generics
from drf_spectacular.utils import extend_schema

from apps.bids.models import Bid
from apps.bids.serializers import (BidDetailSerializer,)


@extend_schema(
    tags=["Bids"],
    summary="List bid history",
    description="Return paginated bid history for an auction.",
    responses=BidDetailSerializer,
)
class BidHistoryView( generics.ListAPIView):
    serializer_class = (BidDetailSerializer)

    def get_queryset(self):

        return (
            Bid.objects.filter(auction_id=self.kwargs[ "auction_id"]).select_related("bidder", "auction")
        )
