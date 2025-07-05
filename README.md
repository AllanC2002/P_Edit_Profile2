# Edit Profile Microservice

## Folder Structure

The project is organized into the following folders:

*   **`.github/`**: Contains GitHub Actions workflows, such as the `docker-publish.yml` workflow for automating Docker image builds and publishing.
*   **`conections/`**: This directory is responsible for managing database connections. It includes `mysql.py`, which likely contains functions to establish connections with MySQL databases (one for user accounts and another for user profiles).
*   **`models/`**: Defines the data structures and database schema. `models.py` uses SQLAlchemy to define ORM (Object-Relational Mapper) models for entities like `User`, `Profile`, `Type`, and `Preference`, representing tables in the respective databases.
*   **`services/`**: Contains the business logic of the application. `functions.py` includes functions like `edit_user`, which orchestrates operations such as updating user information in multiple database tables.
*   **`tests/`**: Includes test files for the application. `route_test.py` appears to be an integration test for the API endpoints, while `test_edit_user.py` likely contains unit tests for the `edit_user` service function.
*   **`__pycache__/`**: This is a directory automatically created by Python to store bytecode cache files (`.pyc`). It's generally not tracked by version control.

## Backend Design Pattern

The backend appears to follow a **Layered Architecture**.

*   **Presentation Layer (API Endpoints)**: `main.py` defines the API endpoints using Flask (e.g., `/update-user`). It handles incoming HTTP requests, authentication, and basic request validation.
*   **Service Layer**: The `services/` directory encapsulates the core business logic. Functions within `services/functions.py` (like `edit_user`) coordinate data access and manipulation, acting as an intermediary between the API endpoints and the data access layer.
*   **Data Access Layer**: The `conections/` directory and `models/models.py` together form the data access layer. `conections/mysql.py` manages the database connections, and `models/models.py` defines the ORM entities that map to database tables. SQLAlchemy is used for database interactions.

This separation of concerns allows for better maintainability and testability.

## Communication Architecture

The application exposes a **RESTful API** over HTTP.

*   **Protocol**: HTTP/HTTPS
*   **Data Format**: JSON is used for request and response bodies.
*   **Authentication**: **JSON Web Tokens (JWT)** are used for securing endpoints.
    *   The client must include an `Authorization` header with a `Bearer` token in requests to protected endpoints.
    *   The `main.py` file includes logic to decode and verify JWTs using a `SECRET_KEY`.

## Folder Pattern

The project primarily uses a **Layer-based folder pattern**. The code is organized by its technical responsibility:

*   `main.py`: Entry point and API routing (Presentation Layer)
*   `services/`: Business logic (Service Layer)
*   `conections/` & `models/`: Data access and persistence (Data Access Layer)
*   `tests/`: Testing

## Endpoint Instructions

### Update User Information

*   **Endpoint**: `/update-user`
*   **Method**: `PATCH`
*   **Description**: Modifies the name, lastname, and/or password of an existing user.
*   **Authentication**: Required. A valid JWT must be provided in the `Authorization` header.
    *   **Header**: `Authorization: Bearer <your_jwt_token>`
*   **Request Body**: JSON object containing the fields to update.
    ```json
    {
        "Name": "NewName",
        "Lastname": "NewLastname",
        "Password": "NewSecurePassword123"
    }
    ```
    *   `Name` (optional): The new first name of the user.
    *   `Lastname` (optional): The new last name of the user.
    *   `Password` (optional): The new password for the user. It will be hashed before being stored.
*   **Responses**:
    *   **`200 OK`**: User data updated successfully.
        ```json
        {
            "message": "User data updated successfull"
        }
        ```
    *   **`401 Unauthorized`**:
        *   Token missing or invalid format.
            ```json
            {
                "error": "Token missing or invalid"
            }
            ```
        *   Invalid token data (e.g., `user_id` not found in token).
            ```json
            {
                "error": "Invalid token data"
            }
            ```
        *   Token expired.
            ```json
            {
                "error": "Token expired"
            }
            ```
        *   Invalid token.
            ```json
            {
                "error": "Invalid token"
            }
            ```
    *   **`404 Not Found`**: Active user or profile not found for the `Id_User` extracted from the token.
        ```json
        {
            "error": "Active user/profile not found"
        }
        ```
