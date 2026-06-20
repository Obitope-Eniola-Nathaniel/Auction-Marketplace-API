from decimal import Decimal
from datetime import timedelta

import pytest
from django.utils import timezone

from apps.auctions.services.create_auction import (
    CreateAuctionService,
)

from tests.factories.user_factory import (
    UserFactory,
)


@pytest.mark.django_db
def test_create_auction():

    owner = UserFactory()

    auction = CreateAuctionService.execute(
        owner=owner,
        title="MacBook Pro",
        description="2024 model",
        starting_price=Decimal("500.00"),
        end_time=timezone.now() + timedelta(days=1),
    )

    assert auction.id is not None
    assert auction.owner == owner
    assert auction.starting_price == Decimal("500.00")
    assert auction.current_price == Decimal("500.00")