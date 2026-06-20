from rest_framework import serializers


class AuctionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    starting_price = serializers.DecimalField(max_digits=12, decimal_places=2)
    end_time = serializers.DateTimeField()

    def validate_starting_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Starting price must be greater than zero.")
        
        return value