from rest_framework import serializers

from .auction_image import AuctionImageSerializer
from apps.auctions.models import Auction


class AuctionDetailSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()
    winner = serializers.StringRelatedField()

    images = AuctionImageSerializer( many=True,read_only=True,)

    class Meta:
        model = Auction

        fields = (
            "id",
            "title",
            "description",
            "starting_price",
            "current_price",
            "status",
            "end_time",
            "owner",
            "winner",
            "images",
            "created_at",
            "updated_at",
        )