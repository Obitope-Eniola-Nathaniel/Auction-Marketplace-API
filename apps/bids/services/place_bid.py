from django.db import transaction
from apps.bids.models import Bid
from apps.common.exceptions.custom_exceptions import (BusinessRuleViolation,)
from apps.auctions.models.choices import AuctionStatus


class PlaceBidService:

    @staticmethod
    @transaction.atomic
    def execute(*, auction,  bidder, amount,):
        auction = (auction.__class__.objects.select_for_update() .get(pk=auction.pk))

        if auction.owner_id == bidder.id:
            raise BusinessRuleViolation("You cannot bid on your own auction.")

        if auction.status != AuctionStatus.ACTIVE:
            raise BusinessRuleViolation("Auction is not active.")

        if auction.is_expired:
            raise BusinessRuleViolation("Auction has expired.")

        if amount <= auction.current_price:
            raise BusinessRuleViolation("Bid must be higher than current price.")

        bid = Bid.objects.create(auction=auction, bidder=bidder,amount=amount,)

        auction.current_price = amount
        auction.save(update_fields=["current_price"])

        return bid