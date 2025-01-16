# IMDb Clone 🎥
A Django-based web application that replicates the functionality of IMDb, enabling users to browse, review, and manage a watchlist for movies and shows on various streaming platforms.

## 🌟 Features
### Streaming Platforms:
+ Manage streaming platforms like Netflix, Hulu, and Amazon Prime.
+ Add, update, and delete platforms with their details.

### Watchlist:
+ Add and manage a watchlist of movies or shows.
+ View movie details, including average ratings and the number of reviews.

### User Reviews:
+ Authenticated users can leave ratings and reviews for movies/shows (1–5 stars).
+ Users can edit or delete their reviews.

### User Management:
+ User registration and authentication using token-based authentication.
+ Admins can delete user accounts.

### API Features:
+ Fully functional REST API for managing movies, platforms, and reviews.
+ Pagination, filtering, and search functionality for movies and platforms.

### Throttling:
+ Custom throttle rates for anonymous and authenticated users.
+ Scoped throttling for specific actions like review creation.

## 🛠️ Tech Stack
+ Backend: Django, Django REST Framework
+ Database: PostgreSQL
+ Authentication: Token-based authentication
+ Libraries:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- django-filter for filtering and searching.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- psycopg2 for PostgreSQL integration.<br>

## 🚀 Installation and Setup
### Prerequisites:
+ Python 3.9+
+ PostgreSQL installed and configured.

### Clone the Repository:
+ git clone <repository-url>
+ cd imdb-clone

### Set Up Virtual Environment:
+ python -m venv venv
+ source venv/bin/activate

### Install Dependencies:
+ pip install -r requirements.txt

### Configure Database: Update DATABASES in settings.py with your PostgreSQL credentials:
DATABASES = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;'default': {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'ENGINE': 'django.db.backends.postgresql',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'NAME': 'Imdb_project',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'USER': 'Bala',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'PASSWORD': '******',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HOST': 'localhost',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'PORT': '5432',<br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
}

### Apply Migrations:
+ python manage.py makemigrations
+ python manage.py migrate

### Create a Superuser:
+ python manage.py createsuperuser

### Run the Server:
+ python manage.py runserver<br>
Access the app at http://127.0.0.1:8000.

## 📚 API Endpoints
### Streaming Platforms
+ GET /stream/ - List all platforms.
+ POST /stream/ - Add a new platform.
+ GET /stream/<int:pk> - Retrieve, update, or delete a specific platform.
### Watchlist
+ GET /watchlist/ - List all movies/shows.
+ POST /watchlist/ - Add a new movie/show.
+ GET /watchlist/<int:pk> - Retrieve, update, or delete a specific movie/show.
### Reviews
+ GET /stream/<int:pk>/review/ - List all reviews for a movie.
+ POST /stream/<int:pk>/review-create/ - Add a review for a movie.
+ GET /stream/review/<int:pk> - Retrieve, update, or delete a specific review.
+ GET /stream/reviews/<str:username>/ - View all reviews by a specific user.
### User Authentication
+ POST /register/ - User registration.
+ POST /logout/ - User logout.

## 🧪 Running Tests
### Run the test suite with:
+ python manage.py test

## 🌟 Future Enhancements
### Template Rendering:
+ Build dynamic, user-friendly web pages using Django templates to enhance the frontend and improve the user experience.

### Portfolio Feature:
+ Add a portfolio section where users can showcase their favorite movies or reviews they've written. This will act as a personalized collection or watchlist to share with others.

### OAuth-Based Authentication:
+ Implement login options via Google, Facebook, or other OAuth providers for a seamless user authentication experience.

### Image Uploads:
+ Add support for uploading and displaying posters or images for movies and shows.

### Notification System:
+ Notify users of new reviews, platform updates, or recommendations based on their watchlist.

### Performance Optimization:
+ Use caching to optimize API performance and reduce server response time for frequently accessed data.

## 🤝 Credits
+ Developed by: Bala Raju.K
+ Framework: Django and Django REST Framework
+ Database: PostgreSQL

## 📄 License
+ This project is licensed under the MIT License. See the LICENSE file for more details.
