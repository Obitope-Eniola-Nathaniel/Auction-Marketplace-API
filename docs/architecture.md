# Architecture

This project is organized by product domain:

- `apps.users`: authentication, roles, and user profile concerns.
- `apps.auctions`: auction listings and listing permissions.
- `apps.bids`: bidding flow and bid history.
- `apps.common`: shared base models, permissions, exceptions, and utilities.

Each domain can grow using the same pattern: `models`, `serializers`, `views`, `services`, `urls`, and `tests`.
