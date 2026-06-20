from django.db import transaction

from apps.auctions.models.choices import AuctionStatus


class CompleteAuctionService:

    @staticmethod
    @transaction.atomic
    def execute(*, auction):

        highest_bid = (
            auction.bids
            .select_related("bidder")
            .order_by("-amount")
            .first()
        )

        if highest_bid:
            auction.winner = highest_bid.bidder

        auction.status = AuctionStatus.COMPLETED

        auction.save()

        return auction