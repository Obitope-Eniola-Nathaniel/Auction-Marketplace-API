import factory

from apps.users.models import User
from apps.users.models.choices import UserRole


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(
        lambda n: f"user{n}"
    )

    email = factory.Sequence(
        lambda n: f"user{n}@test.com"
    )

    password = factory.PostGenerationMethodCall(
        "set_password",
        "password123"
    )

    role = UserRole.USER