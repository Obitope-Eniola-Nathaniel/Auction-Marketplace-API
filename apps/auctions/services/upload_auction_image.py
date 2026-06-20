import cloudinary.uploader

from apps.auctions.models import (AuctionImage,)


class UploadAuctionImageService:

    @staticmethod
    def execute(*,auction,image,):

        result = (
            cloudinary.uploader.upload(
                image,
                folder="auction-marketplace",
            )
        )

        auction_image = (
            AuctionImage.objects.create(
                auction=auction,
                image_url=result["secure_url"],
                public_id=result["public_id"],
            )
        )

        return auction_image