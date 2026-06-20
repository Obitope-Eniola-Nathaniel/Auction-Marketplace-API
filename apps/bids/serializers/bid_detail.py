from rest_framework import serializers

from apps.bids.models import Bid


class BidDetailSerializer(serializers.ModelSerializer):

    bidder = serializers.StringRelatedField()

    class Meta:
        model = Bid

        fields = (
            "id",
            "bidder",
            "amount",
            "created_at",
        )