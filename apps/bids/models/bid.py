from django.conf import settings
from django.db import models

from apps.common.models.base import TimeStampedModel


class Bid(TimeStampedModel):
    auction = models.ForeignKey("auctions.Auction", on_delete=models.CASCADE, related_name="bids",)
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=12, decimal_places=2,)

    class Meta:
        db_table = "bids"
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["auction"]),
            models.Index(fields=["bidder"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self) -> str:
        return (
            f"{self.bidder.username} "
            f"bid {self.amount} "
            f"on {self.auction.title}"
        )