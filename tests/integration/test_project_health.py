import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.django_db
def test_custom_user_model_creates_user():
    user = get_user_model().objects.create_user(
        username="auction_user",
        email="auction@example.com",
        password="StrongPass123",
    )

    assert user.username == "auction_user"
    assert user.role == "USER"
    assert user.check_password("StrongPass123")


def test_register_route_is_available():
    assert reverse("auth-register") == "/api/auth/register/"
