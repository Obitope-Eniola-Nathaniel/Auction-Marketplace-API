from apps.auctions.models import Auction
from apps.common.exceptions.custom_exceptions import (BusinessRuleViolation,)


class CreateAuctionService:

    @staticmethod
    def execute(*, owner, title, description, starting_price, end_time):
        auction = Auction.objects.create(
            owner=owner,
            title=title,
            description=description,
            starting_price=starting_price,
            current_price=starting_price,
            end_time=end_time,
        )

        return auction
    

