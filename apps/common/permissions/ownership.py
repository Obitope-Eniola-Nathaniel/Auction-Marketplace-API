from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrAdmin(BasePermission):
    """Allow read access to everyone, writes to owners and admins."""

    owner_field = "owner"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_staff or getattr(user, "role", None) == "ADMIN":
            return True

        owner = getattr(obj, self.owner_field, None)
        return owner == user
