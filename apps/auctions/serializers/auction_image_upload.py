from rest_framework import serializers


class AuctionImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True,  allow_empty_file=False, use_url=False,)

    def validate_image(self, value):

        max_size = 5 * 1024 * 1024

        if value.size > max_size:
            raise serializers.ValidationError("Image size cannot exceed 5MB.")

        return value


