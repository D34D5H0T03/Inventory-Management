# Inventory & Point of Sale (POS) API

A RESTful backend API built with Django and Django REST Framework (DRF) to manage store inventory, pricing, and point-of-sale operations. 

**Note:** This repository exclusively contains the backend API layer. It is designed to act as the data and authentication provider for a decoupled frontend client currently being built with **React**. 

## Tech Stack

*   **Framework:** Django & Django REST Framework (DRF)
*   **Database:** PostgreSQL (via `psycopg2-binary`)
*   **Authentication:** JSON Web Tokens (via `djangorestframework-simplejwt`)
*   **Environment Management:** `python-dotenv`

## System Architecture

### Data Normalization (Models)
The database utilizes a relational tree structure to eliminate data redundancy and maintain referential integrity using `CASCADE` deletion.

*   **Category:** Represents broader product classifications (e.g., Beverages, Produce). 
*   **Product:** Represents individual items for sale, linked to a single Category via a Foreign Key (One-to-Many relationship).

### Role-Based Access Control (RBAC)
Security and endpoint access are governed by Django's native permission system combined with DRF's `DjangoModelPermissions`. 

*   **Admin/Superuser:** Full CRUD access to all system data and configurations.
*   **Manager:** Full CRUD access to Categories and Products.
*   **Cashier:** Read-only access to Categories and Products (can view catalog/prices for checkout, but cannot alter stock or pricing).

## API Endpoints

Traffic is routed through a DRF `DefaultRouter`, providing standard CRUD operations. All endpoints (except the JWT generation) require a valid `Bearer <Token>` in the Authorization header.

### Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/token/` | Accepts credentials and returns an Access/Refresh JWT pair. |
| `POST` | `/api/token/refresh/` | Accepts a valid refresh token and returns a new access token. |

### Inventory Management
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/categories/` | Returns a list of all categories. |
| `POST` | `/api/categories/` | Creates a new category. |
| `GET` | `/api/categories/<id>/` | Returns details for a specific category. |
| `PUT/PATCH` | `/api/categories/<id>/` | Updates a specific category. |
| `DELETE` | `/api/categories/<id>/` | Deletes a category (cascades to associated products). |
| `GET` | `/api/products/` | Returns a list of all products, including their category IDs. |
| `POST` | `/api/products/` | Creates a new product. |
| `GET` | `/api/products/<id>/` | Returns details for a specific product. |
| `PUT/PATCH` | `/api/products/<id>/` | Updates a specific product. |
| `DELETE` | `/api/products/<id>/` | Deletes a specific product. |

## Development Status
This API is currently in active local development. Deployment instructions and environment variable configurations will be added once the React frontend integration is complete and the system is prepared for production hosting.
