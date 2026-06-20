from decimal import Decimal

import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import (
    RefreshToken,
)

from tests.factories.user_factory import (
    UserFactory,
)

from tests.factories.auction_factory import (
    AuctionFactory,
)


def authenticate(client, user):

    token = RefreshToken.for_user(user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token.access_token}"
    )


@pytest.mark.django_db
def test_place_bid():

    owner = UserFactory()

    bidder = UserFactory()

    auction = AuctionFactory(
        owner=owner
    )

    client = APIClient()

    authenticate(client, bidder)

    response = client.post(
        f"/api/bids/{auction.id}/bids/",
        {
            "amount": "200.00"
        },
        format="json",
    )

    assert response.status_code == 201

    assert response.data["amount"] == "200.00"


@pytest.mark.django_db
def test_bid_history():

    owner = UserFactory()

    bidder = UserFactory()

    auction = AuctionFactory(
        owner=owner
    )

    client = APIClient()

    authenticate(client, bidder)

    client.post(
        f"/api/bids/{auction.id}/bids/",
        {
            "amount": "200.00"
        },
        format="json",
    )

    response = client.get(
        f"/api/bids/{auction.id}/bids/history/"
    )

    assert response.status_code == 200