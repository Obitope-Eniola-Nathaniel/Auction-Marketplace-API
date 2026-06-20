from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated,)
from rest_framework.response import Response
from rest_framework import status

from apps.auctions.models import Auction
from apps.bids.serializers import (BidCreateSerializer,BidDetailSerializer,)
from apps.bids.services import (PlaceBidService,)


class CreateBidView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, auction_id,):
        serializer = (BidCreateSerializer(data=request.data))

        serializer.is_valid(raise_exception=True)

        auction = Auction.objects.get(pk=auction_id)

        bid = PlaceBidService.execute(
            auction=auction,
            bidder=request.user,
            amount=serializer.validated_data["amount"],
        )

        return Response(BidDetailSerializer(bid).data, status=status.HTTP_201_CREATED, )