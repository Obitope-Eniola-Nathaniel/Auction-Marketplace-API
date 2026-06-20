from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from apps.auctions.models import Auction
from apps.auctions.serializers import (AuctionCreateSerializer, AuctionDetailSerializer, AuctionListSerializer,)
from apps.auctions.services import CreateAuctionService


@extend_schema(
    tags=["Auctions"],
    description="List active auction listings or create a new auction.",
)
class AuctionListCreateView(generics.ListCreateAPIView):
    queryset = (Auction.objects.select_related("owner").all())

    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="List auctions",
        responses=AuctionListSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create auction",
        request=AuctionCreateSerializer,
        responses=AuctionListSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):

        if self.request.method == "POST":
            return AuctionCreateSerializer

        return AuctionListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auction = CreateAuctionService.execute(owner=request.user, **serializer.validated_data)
        return Response(AuctionDetailSerializer(auction).data, status=status.HTTP_201_CREATED)
