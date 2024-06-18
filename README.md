# Blogging Application

This is a simple blogging application built using Django. Users can create and manage blog posts, and readers can view and comment on the posts.

## Features

- User authentication (sign up, log in, log out)
- Create, read, update, and delete blog posts
- Comment on posts
- View a list of all blog posts
- View individual blog posts with comments

## Requirements

- Python 3.x
- Django 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yashovardhn/blogging.git
    ```

2. Navigate to the project directory:

    ```bash
    cd blogging
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your web browser and go to `http://127.0.0.1:8000` to see the application running.

## Usage

1. Sign up for an account or log in using the credentials you created.
2. Create and manage blog posts through the user interface.
3. Comment on blog posts.
4. View a list of all blog posts and individual blog posts with comments.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please contact [yashovardhn](https://github.com/yashovardhn).
