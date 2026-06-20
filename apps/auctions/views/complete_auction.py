from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated,)
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from apps.auctions.models import Auction
from apps.auctions.services import (CompleteAuctionService,)


class CompleteAuctionResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class CompleteAuctionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompleteAuctionResponseSerializer

    @extend_schema(
        tags=["Auctions"],
        summary="Complete auction",
        description="Mark an auction as completed and assign the highest bidder as winner.",
        responses={200: CompleteAuctionResponseSerializer},
    )
    def post(self,request,pk):
        auction = get_object_or_404(Auction.objects.select_related("owner", "winner"), pk=pk)

        CompleteAuctionService.execute(auction=auction)

        return Response(
            {
                "message":
                "Auction completed."
            },
            status=status.HTTP_200_OK,
        )
