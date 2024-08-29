# Handheld Tracker

This is the backend for the Handheld Tracker project, built using Django and Django REST Framework. The purpose of this project is to manage and track a collection of handheld consoles. The backend provides API endpoints for authentication, console data management, and user-specific data. The frontend part of this project can be found [here](https://github.com/rene-ruiz/handheld-tracker-next).

## Features

- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT) with token refresh and blacklisting capabilities.
- **Console Management**: APIs to retrieve a list of console items including details like name, company, description, and original price.
- **User Console Collection**: Track which consoles are owned by each user, with timestamps for when they were added.
- **Favorite Consoles**: Mark consoles as favorites for authenticated users, automatically determined based on ownership.
- **CORS Support**: Configured to allow cross-origin requests from specific frontend hosts.
- **Pre-commit Hook Integration**: Pre-commit setup for code quality checks using tools like `black`, `ruff`, etc.

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rene-ruiz/handheld-tracker-backend.git
    cd handheld-tracker-backend
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install precommit hooks:**
    ```
    pre-commit install
    ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Load the initial data** (if any):
    ```bash
    python manage.py loaddata initial_console_list
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure

- **console_list**: Handles the management of console items and user ownership.
- **authentication**: Provides user authentication, registration, and JWT-based login functionality.
- **core**: The main project settings and configuration files.

## API Endpoints

### Authentication
- `POST /api/register/` - Register a new user
- `POST /api/login/` - Login and retrieve JWT tokens
- `POST /api/logout/` - Logout and blacklist the current token
- `POST /api/token/refresh/` - Refresh the access token
- `GET /api/userinfo/` - Retrieve logged-in user details

### Console Management
- `GET /api/consoles/` - Retrieve a list of all available consoles
- `GET /api/consoles/<id>/` - Retrieve details of a specific console

### User Console Collection
- `GET /api/user-consoles/` - Retrieve the logged-in user's console collection
- `POST /api/user-consoles/` - Add a console to the logged-in user's collection

## Dependencies

- Django 5.1
- Django REST Framework 3.15.2
- Django CORS Headers 4.4.0
- Django REST Framework SimpleJWT 5.3.1
- Pre-commit 3.8.0
