from rest_framework import serializers


class AuctionUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    end_time = serializers.DateTimeField(required=False)
