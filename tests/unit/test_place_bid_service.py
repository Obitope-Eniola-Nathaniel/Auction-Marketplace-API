from decimal import Decimal
from datetime import timedelta

import pytest
from django.utils import timezone

from apps.bids.services.place_bid import (
    PlaceBidService,
)

from apps.common.exceptions.custom_exceptions import (
    BusinessRuleViolation,
)

from tests.factories.user_factory import (
    UserFactory,
)

from tests.factories.auction_factory import (
    AuctionFactory,
)


@pytest.mark.django_db
def test_successful_bid():

    owner = UserFactory()

    bidder = UserFactory()

    auction = AuctionFactory(
        owner=owner,
        current_price=Decimal("100.00"),
    )

    bid = PlaceBidService.execute(
        auction=auction,
        bidder=bidder,
        amount=Decimal("150.00"),
    )

    auction.refresh_from_db()

    assert bid.amount == Decimal("150.00")
    assert auction.current_price == Decimal("150.00")


@pytest.mark.django_db
def test_owner_cannot_bid():

    owner = UserFactory()

    auction = AuctionFactory(
        owner=owner
    )

    with pytest.raises(
        BusinessRuleViolation
    ):
        PlaceBidService.execute(
            auction=auction,
            bidder=owner,
            amount=Decimal("150.00"),
        )


@pytest.mark.django_db
def test_bid_must_be_higher():

    owner = UserFactory()

    bidder = UserFactory()

    auction = AuctionFactory(
        owner=owner,
        current_price=Decimal("100.00"),
    )

    with pytest.raises(
        BusinessRuleViolation
    ):
        PlaceBidService.execute(
            auction=auction,
            bidder=bidder,
            amount=Decimal("100.00"),
        )


@pytest.mark.django_db
def test_expired_auction_rejects_bid():

    owner = UserFactory()

    bidder = UserFactory()

    auction = AuctionFactory(
        owner=owner,
        end_time=timezone.now()
        - timedelta(days=1),
    )

    with pytest.raises(
        BusinessRuleViolation
    ):
        PlaceBidService.execute(
            auction=auction,
            bidder=bidder,
            amount=Decimal("200.00"),
        )