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
def test_create_auction():

    user = UserFactory()

    client = APIClient()

    authenticate(client, user)

    payload = {
        "title": "MacBook Pro",
        "description": "M3 Max",
        "starting_price": "1000.00",
        "end_time": "2030-01-01T12:00:00Z",
    }

    response = client.post(
        "/api/auctions/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    assert response.data["title"] == "MacBook Pro"


@pytest.mark.django_db
def test_owner_can_update_auction():

    owner = UserFactory()

    auction = AuctionFactory(
        owner=owner
    )

    client = APIClient()

    authenticate(client, owner)

    response = client.patch(
        f"/api/auctions/{auction.id}/",
        {
            "title": "Updated Title"
        },
        format="json",
    )

    assert response.status_code in [200, 202]


@pytest.mark.django_db
def test_non_owner_cannot_update():

    owner = UserFactory()

    stranger = UserFactory()

    auction = AuctionFactory(
        owner=owner
    )

    client = APIClient()

    authenticate(client, stranger)

    response = client.patch(
        f"/api/auctions/{auction.id}/",
        {
            "title": "Hacked"
        },
        format="json",
    )

    assert response.status_code == 403