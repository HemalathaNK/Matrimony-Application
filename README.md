# Matrimony Application

## Overview

This project is a Matrimony Application built using Python and Django for backend operations and HTML, CSS, and JavaScript for the frontend. The application allows users to register, create profiles, search for potential matches, and communicate securely.

## Technologies Used

__Backend:__ Python, Django

__Frontend:__ HTML, CSS, JavaScript

__Database:__ MySQL (via MySQL Workbench)

__IDE:__ VS Code

## Features

* **User Registration & Login:** Secure authentication using Django's built-in authentication system.

* **Profile Management:** Users can create and update their profiles with personal details.

* **Search Functionality:** Users can search for matches based on specific filters.

* **Admin Dashboard:** Admins can manage user profiles and monitor activities.

## Requirements

### Software

**Python 3.x:** Required to run the Django server.

**VS Code:** For coding and development.

**MySQL Workbench:** To manage MySQL database.

### Libraries & Packages

Install the required dependencies using pip:

`pip install django pillow mysqlclient virtualenv`

### Installation & Setup

1. **Install Virtual Environment:**

      `pip install virtualenv`

2. **Create a Virtual Environment:**

      `virtualenv venv`

3. **Activate the Virtual Environment:**

      `venv\Scripts\activate`

4. **Create Django Project & App:**

      `django-admin startproject ProjectName
   
       django-admin startapp AppName`

6. **Set up the database:**

      Create a MySQL database named MatrimonyDB in MySQL Workbench.
   
      Update settings.py with database credentials.

8. **Apply Migrations:**

    `python manage.py makemigrations
   
    python manage.py migrate`
   
10. **Create a Superuser (For Admin Access):**

      `python manage.py createsuperuser`

8. **Run the Server:**

      `python manage.py runserver`

      The application will be accessible at: ` http://127.0.0.1:8000`

## Function Explanations

The application maps functions in `views.py` via `urls.py`:

1. `login_fun`: Handles user login by fetching registered data from the database. Redirects males to the female profiles page and females to the male profiles page.

2. `signup_fun`: Handles user registration.

4. `home_page`: Displays all registered users.

5. `brides_profiles`: Displays only female profiles (photo, name, age, job, and a "See Details" button).

6. `grooms_profiles`: Displays only male profiles (photo, name, age, job, and a "See Details" button).

7. `bride_details`: Shows full details of a bride when clicked from brides_profiles.

8. `groom_details`: Shows full details of a groom when clicked from grooms_profiles.

9. `see_details`: Shows complete profile details when accessed from home_page.

10. `profile_fun`: Allows the currently logged-in user to access, update, and delete their profile.

11. `update_profile`: Updates the logged-in user's profile.

12. `delete_profile`: Deletes the logged-in user's profile.

13. `search_profiles`: Provides search functionality for profiles.

14. `logout_fun`: Logs out the user.

## Additional Notes

* The project uses Django ORM for database operations.

* It also utilizes Django Template Language (DTL), also known as Jinja language.

* Ensure you have Django installed before running the project.

* If any errors occur, check the official documentation for troubleshooting.

* Secure user data by configuring Django settings properly.

## Conclusion

This Matrimony Application provides a secure and efficient platform for users to find and communicate with their ideal match. Follow the setup instructions to deploy your application successfully.

## Contact

For further inquiries, contact: hemalathank9207@gmail.com

