# Matrimony Application

## Overview
The Matrimony Application is a web-based platform that allows users to register, search for potential matches, and manage their profiles. It is built using Python, Django, MySQL, HTML, CSS, and JavaScript.

## Technologies Used

__Backend:__ Python, Django

__Frontend:__ HTML, CSS, JavaScript, Boostrap

__Database:__ MySQL (via MySQL Workbench)

__IDE:__ PyCharm

## Features

* **User Registration & Login:** Secure authentication using Django's built-in authentication system.

* **Profile Management:** Users can create and update their profiles with personal details.

* **Search Functionality:** Users can search for matches based on specific filters.
  
* **Forgot Password Feature:** Uses Django’s built-in password reset functionality for forgot password.
  
* **Static and Media File Management:** Static files (CSS, JS) and media files (user profile pictures) are properly configured using static and media files

* **Admin Dashboard:** Admins can manage user profiles and monitor activities.

## Requirements

### Software

**Python 3.x:** Required to run the Django server.

**PyCharm:** For coding and development.

**MySQL Workbench:** To manage MySQL database.

### Libraries & Packages
The Matrimony Application utilizes several libraries and frameworks to handle web development, database management, and user authentication. Below are the key technologies used:

1. **Django:** Django is a high-level Python web framework that enables rapid development of secure and scalable web applications by following the MVT (Model-View-                        Templates) architecture.
2. **MySQLClient:** – Python library for connecting Django with the MySQL database.
3. **Pillow:** Used for handling image uploads 
4. **Virtual Environment:** Used to manage dependencies and isolate the project environment
5. **Django ORM:** – Object-Relational Mapping to interact with the MySQL database.
7. **Django Template Language (Jinja):** Used for rendering dynamic content in HTML templates.

**Install the required dependencies using** `pip`:

Open a terminal or command prompt and run the following command to install all the required libraries:

`pip install django pillow mysqlclient virtualenv`

### Installation & Setup

#### Using Virtual Environments (Recommended)
It's highly recommended to create a virtual environment for this project to isolate its dependencies from other Python projects on your system. You can use tools like venv or virtualenv to create a virtual environment. Refer to their documentation for specific instructions.

Once you have a virtual environment activated, run the pip install command mentioned earlier to install the libraries within the isolated environment.

1. **Install Virtual Environment:**

      `pip install virtualenv`

2. **Create a Virtual Environment:**

      `virtualenv venv`

3. **Activate the Virtual Environment:**

      `venv\Scripts\activate`

4. **Create Django Project & App:**

       `django-admin startproject ProjectName`
   
       `django-admin startapp AppName`

6. **Set up the database:**

      Create a MySQL database named MatrimonyDB in MySQL Workbench.
   
      Update settings.py with database credentials.

8. **Apply Migrations:**

    `python manage.py makemigrations`
   
   ` python manage.py migrate`
   
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

