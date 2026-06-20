from rest_framework import serializers

from apps.auctions.models import Auction


class AuctionListSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    class Meta:
        model = Auction

        fields = (
            "id",
            "title",
            "current_price",
            "status",
            "end_time",
            "owner",
        )