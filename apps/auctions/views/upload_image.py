from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.parsers import ( MultiPartParser,FormParser,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from apps.auctions.models import Auction
from apps.auctions.serializers import ( AuctionImageUploadSerializer, AuctionImageSerializer,)
from apps.auctions.services.upload_auction_image import ( UploadAuctionImageService,)


class UploadAuctionImageView(APIView):

    permission_classes = [IsAuthenticated]

    parser_classes = [ MultiPartParser,  FormParser, ]

    @extend_schema(
        tags=["Auctions"],
        summary="Upload auction image",
        description="Upload an image for an auction.",
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "image": {
                        "type": "string",
                        "format": "binary",
                    }
                },
                "required": ["image"],
            }
        },
        responses={201: AuctionImageSerializer},
    )
    def post(self, request, auction_id):

        auction = get_object_or_404(Auction, pk=auction_id,  )

        serializer = AuctionImageUploadSerializer(data=request.data)

        serializer.is_valid( raise_exception=True )

        image = UploadAuctionImageService.execute( auction=auction, image=serializer.validated_data["image"], )

        return Response(
            AuctionImageSerializer(image).data,
            status=status.HTTP_201_CREATED,
        )