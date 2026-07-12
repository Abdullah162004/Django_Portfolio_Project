# Django Portfolio Website

A personal portfolio website built with Django. It has three pages: Home, Projects, and Contact. The Contact page includes a working form that saves submissions to an SQLite database and displays them in the Django admin panel.

## Features

- Home page with introduction, about section, education, skills, and career goal
- Projects page listing project cards pulled from the database
- Contact page with a form (name, email, subject, message) saved to the database
- Django admin panel for managing Contact, Project, and Skill entries
- Django templates with a shared base.html for navbar and footer
- Static files (CSS, images) served through Django's static file system

## Project Structure

```
django_portfolio/
    manage.py
    portfolio_project/
        settings.py
        urls.py
    portfolio/
        models.py
        views.py
        forms.py
        urls.py
        admin.py
        migrations/
    templates/
        portfolio/
            base.html
            home.html
            projects.html
            contact.html
    static/
        portfolio/
            css/style.css
            images/
    media/
        projects/
```

## Setup Instructions

1. Clone the repository
```
git clone <your-repo-url>
cd django_portfolio
```

2. Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
On Windows use `venv\Scripts\activate`

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run migrations
```
python manage.py migrate
```

5. Create a superuser to access the admin panel
```
python manage.py createsuperuser
```

6. Run the development server
```
python manage.py runserver
```

7. Visit the site at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`

## Adding Content

- Add Skill entries from the admin panel to populate the Skills section on the Home page
- Add Project entries from the admin panel to populate the Projects page
- Submitted Contact form messages appear under the Contact model in the admin panel

## Editing Personal Details

Replace the placeholder text in `templates/portfolio/home.html` with your own name, introduction, education, and career goal. Replace `static/portfolio/images/profile.jpg` with your own profile picture.
