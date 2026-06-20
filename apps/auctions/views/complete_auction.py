from rest_framework.views import APIView
from rest_framework.permissions import (IsAuthenticated,)
from rest_framework.response import Response
from rest_framework import status

from apps.auctions.models import Auction
from apps.auctions.services import (CompleteAuctionService,)


class CompleteAuctionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk):
        auction = Auction.objects.get(pk=pk)

        CompleteAuctionService.execute(auction=auction)

        return Response(
            {
                "message":
                "Auction completed."
            },
            status=status.HTTP_200_OK,
        )