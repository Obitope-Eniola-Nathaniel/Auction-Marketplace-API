from rest_framework import serializers


class AuctionUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)   
    description = serializers.CharField()
    end_time = serializers.DateTimeField()