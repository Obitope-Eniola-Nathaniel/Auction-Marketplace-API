from django.db import models

from apps.common.models.base import TimeStampedModel


class AuctionImage(TimeStampedModel):

    auction = models.ForeignKey("auctions.Auction", on_delete=models.CASCADE,related_name="images",)
    image_url = models.URLField()
    public_id = models.CharField(max_length=255)

    class Meta:
        db_table = "auction_images"

    def __str__(self):
        return self.image_url