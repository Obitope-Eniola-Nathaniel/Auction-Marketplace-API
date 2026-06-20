from decimal import Decimal

import factory

from apps.bids.models import Bid

from tests.factories.user_factory import UserFactory
from tests.factories.auction_factory import AuctionFactory


class BidFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Bid

    auction = factory.SubFactory(
        AuctionFactory
    )

    bidder = factory.SubFactory(
        UserFactory
    )

    amount = Decimal("150.00")