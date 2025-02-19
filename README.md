Matrimony Application

Overview

This project is a Matrimony Application built using Python and Django for backend operations and HTML, CSS, and JavaScript for the frontend. The application allows users to register, create profiles, search for potential matches, and communicate securely.

Technologies Used

Backend: Python, Django

Frontend: HTML, CSS, JavaScript

Database: MySQL

IDE: VS Code

Features

User Registration & Login: Secure authentication using Django's built-in authentication system.

Profile Management: Users can create and update their profiles with personal details.

Search Functionality: Users can search for matches based on specific filters.

Match Recommendations: Intelligent suggestions based on user preferences.

Secure Communication: Users can communicate through a secure messaging system.

Admin Dashboard: Admins can manage user profiles and monitor activities.

Requirements

Software

Python 3.x: Required to run the Django server.

VS Code: For coding and development.

XAMPP: To manage MySQL database.

Libraries

Install the required dependencies using pip:

pip install django mysql-connector-python

Installation & Setup

Clone the repository:

git clone https://github.com/your-repo/matrimony-app.git
cd matrimony-app

Set up a virtual environment (Recommended):

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

Install dependencies:

pip install -r requirements.txt

Set up the database:

Create a MySQL database named matrimony_db.

Update settings.py with database credentials.

Apply Migrations:

python manage.py migrate

Create a Superuser (For Admin Access):

python manage.py createsuperuser

Run the Server:

python manage.py runserver

The application will be accessible at: http://127.0.0.1:8000

Function Explanations

register(): Handles user registration.

login(): Authenticates users and starts a session.

logout(): Logs out the user and ends the session.

create_profile(): Allows users to add personal details.

search_profiles(): Filters and displays potential matches.

send_message(): Enables users to communicate securely.

admin_dashboard(): Provides administrative control over users and profiles.

Additional Notes

Ensure you have Django installed before running the project.

If any errors occur, check the official documentation for troubleshooting.

Secure user data by configuring Django settings properly.

Conclusion

This Matrimony Application provides a secure and efficient platform for users to find and communicate with their ideal match. Follow the setup instructions to deploy your application successfully.

Contact

For further inquiries, contact: hemalathank9207@gmail.com

