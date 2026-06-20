import cloudinary.uploader

from apps.auctions.models import AuctionImage
from apps.common.exceptions.custom_exceptions import (BusinessRuleViolation,)


class UploadAuctionImageService:

    @staticmethod
    def execute(*, auction, image):

        if auction.images.count() >= 5:
            raise BusinessRuleViolation("Maximum of 5 images allowed.")

        result = cloudinary.uploader.upload(image, folder="auction-marketplace", resource_type="image", )

        auction_image = AuctionImage.objects.create(
            auction=auction,
            image_url=result["secure_url"],
            public_id=result["public_id"],
        )

        return auction_image