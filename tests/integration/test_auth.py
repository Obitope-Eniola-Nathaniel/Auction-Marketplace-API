import pytest
from rest_framework.test import APIClient

from apps.users.models import User


@pytest.mark.django_db
def test_register_user():

    client = APIClient()

    payload = {
        "username": "nathaniel",
        "email": "nathaniel@test.com",
        "password": "Password123!",
        "password_confirm": "Password123!",
    }

    response = client.post(
        "/api/auth/register/",
        payload,
        format="json",
    )

    assert response.status_code == 201

    assert User.objects.filter(
        username="nathaniel"
    ).exists()