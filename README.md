# Django Music Website

This project is a simple music website developed using the Django framework. The website provides features for managing songs, artists, albums, and more.

## Installation and Setup

1. Make sure Python and Django are installed on your system.
2. Clone the source code from the GitHub repository to your system:

```bash
git clone https://github.com/AliAnbarlou/MusicVibe.git
```
## Navigate to the project directory and activate the virtual environment:
```bash
cd django-music-website
python -m venv env
source env/bin/activate  # for Unix-based systems
.\env\Scripts\activate   # for Windows
```
## Install dependencies:
```bash
pip install -r requirements.txt
```
## Apply migrations and create the database:
```bash
python3 manage.py migrate
```
## Run the server:
```bash
python manage.py runserver
```
Your website is now accessible at http://localhost:8000/.
#### Important Note
Due to security reasons and site activation, configuration files and database are not available in Github, if you have the necessary experience, create and place them yourself.
## Main Features
-Management of songs, albums, and more.
-Ability to add, edit, and delete various items by site administrators.
-Detailed statistics and charts using django-admin-chart and django-admin-tools-stats.
-Integration with django-taggit for tagging items.
-Image handling using Pillow.
-Database configuration using dj-database-url and python-dotenv for environment variables.
-PostgreSQL database backend using psycopg2-binary.
## Dependencies
-Django
-django-taggit
-django-admin-chart
-django-admin-charts
-django-admin-tools
-django-admin-tools-stats
-django-hitcount
-django-jazzmin
-Pillow
-dj-database-url
-python-dotenv
-psycopg2-binary
