from rest_framework import serializers

from apps.auctions.models import Auction


class AuctionDetailSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()
    winner = serializers.StringRelatedField()

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
            "created_at",
            "updated_at",
        )