# What is this project?

A simple web application which allows users to manage and display food items through django admin panel. It provides a simple interface to add/edit/delete food items, and these items are displayed on the home page.


## Installation

1. Clone the repository:
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin panel (`http://localhost:8000/admin/`) using the superuser credentials created earlier.
- Add food items using the provided interface.
- View the added food items displayed on the index page (`http://localhost:8000/`).

