# Auction Marketplace API

## Overview

Auction Marketplace API is a backend service that allows authenticated users to create auction listings and place bids on active auctions.

The project was built as part of a backend engineering assessment and focuses on clean architecture, maintainability, business rule enforcement, authentication, authorization, testing, and API documentation.

The application supports:

* User registration and authentication
* JWT-based login and logout
* Auction creation and management
* Bid placement
* Bid history tracking
* Auction completion and winner selection
* Role-based access control
* Swagger/OpenAPI documentation

---

# Tech Stack

* Python 3
* Django
* Django REST Framework (DRF)
* PostgreSQL
* Simple JWT
* drf-spectacular (Swagger/OpenAPI)
* pytest
* Factory Boy

---

# Architecture

The project follows a layered architecture to separate concerns and keep business logic maintainable.

```text
Request
    ↓
View
    ↓
Serializer
    ↓
Service
    ↓
Model
    ↓
Database
```

### Why this approach?

Business rules are implemented inside service classes rather than views or serializers.

This keeps:

* Views focused on HTTP handling
* Serializers focused on validation
* Services focused on business logic
* Models focused on persistence

This makes the code easier to test, maintain, and extend.

---

# Project Structure

```text
apps/
│
├── users/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── urls/
│
├── auctions/
│   ├── models/
│   ├── serializers/
│   ├── services/
│   ├── views/
│   ├── urls/
│
├── bids/
│   ├── models/
│   ├── serializers/
│   ├── services/
│   ├── views/
│   ├── urls/
│
├── common/
│   ├── exceptions/
│   ├── permissions/
│   ├── models/
│   └── pagination/
│
config/
│
├── settings/
│   ├── base.py
│   ├── local.py
│   └── production.py
```

---

# Database Design

## User

Represents authenticated users of the platform.

Fields:

* id
* username
* email
* password
* role

Roles:

* USER
* ADMIN

---

## Auction

Represents an auction listing.

Fields:

* owner
* winner
* title
* description
* starting_price
* current_price
* end_time
* status

Statuses:

* ACTIVE
* COMPLETED
* CANCELLED

---

## Bid

Represents a bid placed by a user.

Fields:

* auction
* bidder
* amount
* created_at

---

# Entity Relationships

```text
User
 ├── owns many Auctions
 ├── places many Bids
 └── can win Auctions

Auction
 ├── belongs to User (owner)
 ├── has many Bids
 └── has one winner

Bid
 ├── belongs to Auction
 └── belongs to User
```

---

# Authentication

JWT authentication is implemented using SimpleJWT.

Endpoints:

```http
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/refresh/
POST /api/auth/logout/
```

Logout is implemented using JWT token blacklisting.

---

# Authorization

## User Permissions

Users can:

* Create auctions
* View auctions
* Place bids
* View bid history
* Update their own auctions
* Delete their own auctions

Users cannot:

* Modify another user's auction
* Bid on their own auction

---

## Admin Permissions

Administrators have full access to all auctions.

Administrators can:

* Update any auction
* Delete any auction
* View all auctions

---

# Auction Endpoints

## Auctions

```http
GET    /api/auctions/
POST   /api/auctions/

GET    /api/auctions/{id}/
PATCH  /api/auctions/{id}/
DELETE /api/auctions/{id}/

POST   /api/auctions/{id}/complete/
```

---

## Bids

```http
POST /api/bids/{auction_id}/bids/
GET  /api/bids/{auction_id}/bids/history/
```

---

# Business Rules

The following business rules are enforced through the service layer:

### Auction Creation

* Current price is initialized to the starting price.

### Bid Placement

* Bid amount must be greater than the current auction price.
* Auction owners cannot bid on their own auctions.
* Expired auctions cannot receive bids.
* Completed auctions cannot receive bids.
* Every successful bid is stored in bid history.

### Auction Completion

* Highest bidder becomes the winner.
* Auction status changes to COMPLETED.

---

# Concurrency Handling

To prevent race conditions when multiple users bid at the same time:

```python
select_for_update()
transaction.atomic()
```

are used in the bidding workflow.

This ensures that auction prices remain consistent under concurrent requests.

---

# Error Handling

Global exception handling is implemented using a custom exception handler.

Business rule violations are surfaced through:

```python
BusinessRuleViolation
```

This provides consistent API error responses.

---

# Pagination

Global pagination is enabled for list endpoints.

Examples:

```http
GET /api/auctions/
GET /api/bids/{auction_id}/bids/history/
```

---

# API Documentation

Swagger/OpenAPI documentation is available at:

```text
/api/docs/
/api/schema/
```

A generated OpenAPI specification is also included:

```text
schema.yml
```

---

# Local Setup

## Clone Repository

```bash
git clone <repository-url>
cd auction-marketplace
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements/local.txt
```

## Configure Environment Variables

```bash
copy .env.example .env
```

Update database values as needed.

## Run Migrations

```bash
python manage.py migrate
```

## Start Server

```bash
python manage.py runserver
```

---

# Running Tests

Run all tests:

```bash
pytest -v
```

Generate coverage report:

```bash
coverage run -m pytest
coverage report
```

Generate HTML coverage:

```bash
coverage html
```

---

# Test Coverage

Current test coverage:

```text
96%
```

Coverage includes:

* Service layer tests
* Integration tests
* Authentication tests
* Authorization tests
* Business rule tests

---

# Assumptions

The following assumptions were made:

1. Auction completion is a manual action.
2. Auctions become active immediately after creation.
3. Highest bid amount determines the winner.
4. JWT refresh token blacklisting is used for logout.
5. Users must be authenticated to interact with auctions and bids.

---

# Engineering Decisions

Several engineering decisions were made to improve maintainability:

* Service layer introduced to isolate business logic.
* Domain-based application structure used instead of a flat Django structure.
* PostgreSQL indexes added for commonly queried fields.
* Global exception handling implemented.
* Global pagination enabled.
* Swagger/OpenAPI documentation included.
* JWT token blacklisting implemented for logout.
* Bid placement protected using database row locking.

---

# Future Improvements

If given additional time, the following improvements would be implemented:

* Docker support
* CI/CD with GitHub Actions
* Redis caching
* Celery background jobs
* Automatic auction completion scheduling
* Audit logging
* Rate limiting
* WebSocket-based real-time bidding
* Soft delete support
* Advanced filtering and search
* Email notifications for winners

---

# Author

Nathaniel Obitope

Backend Engineer

Assessment Project – Auction Marketplace API
