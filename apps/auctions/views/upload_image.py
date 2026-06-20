from django.shortcuts import (get_object_or_404,)
from rest_framework.views import (APIView,)
from rest_framework.permissions import (IsAuthenticated,)
from rest_framework.response import ( Response,)
from rest_framework import status
from apps.auctions.models import (Auction,)
from apps.auctions.serializers import (AuctionImageUploadSerializer, AuctionImageSerializer,)
from apps.auctions.services.upload_auction_image import (UploadAuctionImageService,)
from apps.common.permissions.ownership import (IsOwnerOrAdmin,)


class UploadAuctionImageView(APIView):

    permission_classes = [IsAuthenticated, IsOwnerOrAdmin,]

    def post(self, request, auction_id,):

        auction = get_object_or_404(Auction, pk=auction_id,)

        self.check_object_permissions( request, auction,)

        serializer = (AuctionImageUploadSerializer(data=request.data) )

        serializer.is_valid(raise_exception=True )

        image = (
            UploadAuctionImageService.execute(
                auction=auction,
                image=serializer.validated_data["image"],
            )
        )

        return Response(
            AuctionImageSerializer(image ).data,
            status=status.HTTP_201_CREATED,
        )