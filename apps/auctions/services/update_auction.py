from apps.common.exceptions.custom_exceptions import (BusinessRuleViolation,)

class UpdateAuctionService:

    @staticmethod
    def execute(*, auction, **fields):
        if auction.is_expired:
            raise BusinessRuleViolation(
                "Expired auctions cannot be updated."
            )

        for field, value in fields.items():
            setattr(auction, field, value)

        if fields:
            auction.save(update_fields=[*fields.keys(), "updated_at"])

        return auction
