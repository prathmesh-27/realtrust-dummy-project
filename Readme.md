# RealTrust - Dummy Project

A full-stack web application with an **Admin Panel** and **Landing Page** that allows administrators to manage projects, clients, contact form responses, and newsletter subscribers. This project is integrated with **MongoDB Atlas** for backend data storage using `mongoengine`, and follows secure credential management practices via environment variables.

---

## Objective

To create a fully functional admin panel that enables content management for a landing page, specifically focusing on:

- Engaging UI
- Project Showcase
- Client Testimonials
- Contact Form Submissions
- Newsletter Subscriptions

---

## Features

### Admin Panel

#### Project Management
- Add new projects with:
  - Project Image
  - Project Name
  - Project Description

#### Client Management
- Add and manage client details including:
  - Client Image
  - Client Name
  - Client Description
  - Client Designation (e.g., CEO, Web Developer)

#### Contact Form Viewer
- View contact form submissions from users with:
  - Full Name
  - Email Address
  - Mobile Number
  - City

#### Subscribed Users
- View all users who subscribed to the newsletter using their email.

---

### Newsletter Subscription Section
- A public-facing **newsletter section** allows users to enter their email address to subscribe.
- Emails are stored securely in the database and viewable in the admin panel.
---

## Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Frontend      | HTML5, CSS3, JavaScript |
| Backend       | Python (Django) |
| Database      | MongoDB Atlas (NoSQL)    |
| ORM           | mongoengine              |
| Environment   | python-dotenv for `.env` |


## How to run the Project:
### Step 1: Create and Activate Virtual Environment
```
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 2: Installing the requirements

```
pip install -r requirements. txt 
```

### Step 3: Creating .env file

Create a file with name .env and add 

MONGO_DB_NAME= your_db_name
MONGO_USERNAME= your_username
MONGO_PASSWORD= your_password
MONGO_CLUSTER= your_cluster
MONGO_APP_NAME= cluster_name


### Step 4: Start the server using below commands

```
# Apply migrations (won't affect MongoDB structure strictly but required for admin and auth apps)
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```

### Step 5: Access the App
```
Visit:
http://127.0.0.1:8000/ — Your app is now connected to MongoDB Atlas using the credentials from .env.
```
