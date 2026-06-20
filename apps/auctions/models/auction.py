from django.conf import settings
from django.db import models

from apps.common.models.base import TimeStampedModel
from .choices import AuctionStatus


class Auction(TimeStampedModel): 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_auctions",)
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,  null=True, blank=True, related_name="won_auctions",)

    title = models.CharField(max_length=255,)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=12, decimal_places=2,)
    current_price = models.DecimalField(max_digits=12, decimal_places=2,)
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20,choices=AuctionStatus.choices, default=AuctionStatus.ACTIVE,)


    class Meta:
        db_table = "auctions"
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["end_time"]),
            models.Index(fields=["owner"]),
        ]

    def __str__(self) -> str:
        return self.title
    

@property
def is_expired(self):
    from django.utils import timezone

    return timezone.now() >= self.end_time