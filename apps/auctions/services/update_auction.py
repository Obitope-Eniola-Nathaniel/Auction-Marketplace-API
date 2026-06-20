from apps.common.exceptions.custom_exceptions import (BusinessRuleViolation,)

class UpdateAuctionService:

    @staticmethod
    def execute(*, auction, title, description, end_time,):
        if auction.is_expired:
            raise BusinessRuleViolation(
                "Expired auctions cannot be updated."
            )

        auction.title = title
        auction.description = description
        auction.end_time = end_time

        auction.save()

        return auction