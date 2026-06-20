import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories.user_factory import UserFactory
from tests.factories.auction_factory import AuctionFactory
from rest_framework_simplejwt.tokens import (RefreshToken,)


def authenticate(client, user):

    token = RefreshToken.for_user(user)

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token.access_token}"
    )

@pytest.mark.django_db
def test_admin_can_update_any_auction():

    owner = UserFactory()
    admin = UserFactory(is_staff=True)

    auction = AuctionFactory(owner=owner)

    client = APIClient()

    authenticate(client, admin)

    response = client.patch(
        f"/api/auctions/{auction.id}/",
        {
            "title": "Admin Updated"
        },
        format="json",
    )

    assert response.status_code in [200, 202]