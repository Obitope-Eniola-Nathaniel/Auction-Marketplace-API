from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.auctions.models import Auction
from apps.auctions.serializers import (AuctionCreateSerializer, AuctionListSerializer,)
from apps.auctions.services import CreateAuctionService


class AuctionListCreateView(generics.ListCreateAPIView):
    queryset = (Auction.objects.select_related("owner").all())

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):

        if self.request.method == "POST":
            return AuctionCreateSerializer

        return AuctionListSerializer

    def perform_create(self, serializer):
        CreateAuctionService.execute(owner=self.request.user, **serializer.validated_data)