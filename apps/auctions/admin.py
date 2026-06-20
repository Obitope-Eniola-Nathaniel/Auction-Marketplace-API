from django.contrib import admin
from apps.auctions.models import Auction


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "owner",
        "current_price",
        "status",
        "end_time",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "status",
    )