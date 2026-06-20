from django.contrib import admin

from apps.bids.models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "auction",
        "bidder",
        "amount",
        "created_at",
    )

    search_fields = (
        "auction__title",
        "bidder__username",
    )