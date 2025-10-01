# Event Management System

A comprehensive and feature-rich web application for organizing, managing, and attending events. This project showcases a full-stack implementation using Django, with a modern and responsive UI built with Tailwind CSS. It includes advanced features like role-based access control, an RSVP system, user profiles, and optimized database queries.

![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-38B2AC.svg)
![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-brightgreen.svg)

## 🚀 Live Demo

[View Live Application on Render](https://dj-event-mgmt-3.onrender.com/)

## 📋 Project Overview

The Event Management System is designed to provide a seamless experience for three primary user roles: Administrators, Organizers, and Participants. It streamlines the entire event lifecycle, from creation and promotion to registration and management. The application demonstrates proficiency in Django's MVT architecture, ORM, authentication, and modern front-end development practices.

## 🎯 Key Features

### Core Event Management
*   **Full CRUD Operations:** Create, read, update, and delete events, categories, and manage participants.
*   **Event Details:** View comprehensive information for each event, including descriptions, schedules, locations, and participant lists.
*   **Advanced Search & Filtering:** Find events by name or location. Filter events based on their category or a specific date range.
*   **Media Management:** Upload and display event images using Cloudinary.

### User System & Roles
*   **Secure Authentication:** User signup with email verification, login, and logout functionality.
*   **Role-Based Access Control (RBAC):**
    *   **Admin:** Full system access, can manage all users, events, categories, and roles.
    *   **Organizer:** Can create, update, and delete their own events and categories.
    *   **Participant:** Can view events, manage their profile, and RSVP to events.
*   **User-Specific Dashboards:** Each role is redirected to a customized dashboard after login, providing relevant information and tools.

### RSVP & Notifications
*   **RSVP System:** Participants can easily RSVP to events they are interested in attending.
*   **RSVP Management:** Users can view a list of all events they have RSVP'd to in their personal dashboard.
*   **Automated Emails:** Receive confirmation emails upon successful RSVP and account activation notifications, powered by Django Signals.

### User Profiles
*   **Custom User Model:** The default Django User model is extended to include a profile picture and a validated phone number.
*   **Profile Management:** Users can view and edit their profile information, including their name, profile picture, and phone number.
*   **Password Security:** Features for changing and resetting passwords directly from the profile section.

### Technical Highlights
*   **Optimized Database Queries:** Efficient data retrieval using `select_related`, `prefetch_related`, and aggregate queries to minimize database load.
*   **Class-Based Views (CBVs):** The application is refactored to use Django's Class-Based Views for cleaner, more organized, and reusable code.
*   **Responsive UI:** A modern, mobile-first, and visually appealing interface built with Tailwind CSS.
*   **Robust Backend:** Built on the Django framework, following best practices for security and scalability.

## ⚙️ Tech Stack

*   **Backend:** Django, Python
*   **Frontend:** HTML5, Tailwind CSS
*   **Database:** Supabase (PostgreSQL)
*   **Image Storage:** Cloudinary
*   **Deployment:** Render
*   **Version Control:** Git & GitHub

## 🛠️ Installation & Setup

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # On Windows
    # venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**
    Create a `.env` file in the project root and add the following variables:
    ```env
    SECRET_KEY='your-secret-key-here'
    DEBUG=True
    DATABASE_URL='your-supabase-connection-string'
    CLOUDINARY_URL='your-cloudinary-url'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER='your-email@gmail.com'
    EMAIL_HOST_PASSWORD='your-app-password'
    ```

5.  **Run database migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server**
    ```bash
    python manage.py runserver
    ```
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the application.

## 🔐 Admin Access

For demonstration purposes, you can use the following credentials to access the admin panel and explore the Admin role.

> **Note:** These credentials are for the live demo. Please do not change the password.

*   **Admin Username:** `admin`
*   **Admin Password:** `adminpassword`

### Test Users

You can also sign up as a new user or use these pre-configured accounts to test different roles.

*   **Organizer:**
    *   Username: `organizer`
    *   Password: `organizerpassword`
*   **Participant:**
    *   Username: `participant`
    *   Password: `participantpassword`