from rest_framework import serializers
from apps.auctions.models import ( AuctionImage,)


class AuctionImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()



class AuctionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuctionImage

        fields = (
            "id",
            "image_url",
            "created_at",
        )