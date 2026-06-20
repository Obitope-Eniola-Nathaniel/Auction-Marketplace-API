from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.auctions.models import Auction
from apps.auctions.serializers import (AuctionDetailSerializer, AuctionUpdateSerializer,)
from apps.auctions.services import (UpdateAuctionService,)
from apps.common.permissions.ownership import (IsOwnerOrAdmin,)


@extend_schema(tags=["Auctions"])
class AuctionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ( Auction.objects.select_related("owner","winner",))

    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    @extend_schema(
        summary="Retrieve auction",
        responses=AuctionDetailSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update auction",
        request=AuctionUpdateSerializer,
        responses=AuctionDetailSerializer,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update auction",
        request=AuctionUpdateSerializer,
        responses=AuctionDetailSerializer,
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        summary="Delete auction",
        responses={204: None},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_serializer_class(self):

        if self.request.method in ["PATCH", "PUT",]: 
            return AuctionUpdateSerializer

        return AuctionDetailSerializer

    def perform_update(self,serializer,):
        auction = UpdateAuctionService.execute(auction=self.get_object(), **serializer.validated_data,)
        serializer.instance = auction
