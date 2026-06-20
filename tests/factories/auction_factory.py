from decimal import Decimal
from datetime import timedelta

import factory
from django.utils import timezone

from apps.auctions.models import Auction
from apps.auctions.models.choices import AuctionStatus

from tests.factories.user_factory import UserFactory


class AuctionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Auction

    owner = factory.SubFactory(
        UserFactory
    )

    title = factory.Sequence(
        lambda n: f"Auction {n}"
    )

    description = "Test auction"

    starting_price = Decimal("100.00")

    current_price = Decimal("100.00")

    end_time = factory.LazyFunction(
        lambda: timezone.now() + timedelta(days=1)
    )

    status = AuctionStatus.ACTIVE