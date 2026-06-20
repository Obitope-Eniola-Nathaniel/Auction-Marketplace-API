from decimal import Decimal

import pytest

from apps.auctions.services.complete_auction import (
    CompleteAuctionService,
)

from apps.auctions.models.choices import (
    AuctionStatus,
)

from tests.factories.user_factory import (
    UserFactory,
)

from tests.factories.auction_factory import (
    AuctionFactory,
)

from tests.factories.bid_factory import (
    BidFactory,
)


@pytest.mark.django_db
def test_highest_bidder_wins():

    owner = UserFactory()

    bidder_one = UserFactory()

    bidder_two = UserFactory()

    auction = AuctionFactory(
        owner=owner
    )

    BidFactory(
        auction=auction,
        bidder=bidder_one,
        amount=Decimal("150.00"),
    )

    BidFactory(
        auction=auction,
        bidder=bidder_two,
        amount=Decimal("250.00"),
    )

    CompleteAuctionService.execute(
        auction=auction
    )

    auction.refresh_from_db()

    assert auction.winner == bidder_two


@pytest.mark.django_db
def test_auction_marked_completed():

    auction = AuctionFactory()

    CompleteAuctionService.execute(
        auction=auction
    )

    auction.refresh_from_db()

    assert (
        auction.status
        == AuctionStatus.COMPLETED
    )