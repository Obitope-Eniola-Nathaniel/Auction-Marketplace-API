from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.auctions.models import Auction
from apps.auctions.serializers import (AuctionDetailSerializer, AuctionUpdateSerializer,)
from apps.auctions.services import (UpdateAuctionService,)
from apps.common.permissions.ownership import (IsOwnerOrAdmin,)


class AuctionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ( Auction.objects.select_related("owner","winner",))

    permission_classes = [IsAuthenticated, IsOwnerOrAdminForWrite,]

    def get_serializer_class(self):

        if self.request.method in ["PATCH", "PUT",]: 
            return AuctionUpdateSerializer

        return AuctionDetailSerializer

    def perform_update(self,serializer,):
        UpdateAuctionService.execute(auction=self.get_object(), **serializer.validated_data,)