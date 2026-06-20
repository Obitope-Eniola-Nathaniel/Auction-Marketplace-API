from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers.logout import LogoutSerializer


class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


@extend_schema(
    tags=["Authentication"],
    summary="Logout",
    description="Blacklist refresh token and logout user.",
    request=LogoutSerializer,
    responses={
        200: LogoutResponseSerializer,
    },
)
class LogoutView(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):

        serializer = LogoutSerializer(data=request.data)

        serializer.is_valid( raise_exception=True )
        serializer.save()

        return Response(
            {
                "message":
                "Successfully logged out."
            },
            status=status.HTTP_200_OK,
        )