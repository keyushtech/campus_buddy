# Campus Buddy

A lightweight campus portal built with Django to handle daily student utilities—tracking lost & found items, peer-to-peer marketplace listings, and maintenance complaints across hostels and campus departments.

---

## What It Does

- **Lost & Found Tracker**: Post lost or found items with location tags, contact info, and photos.
- **Campus Marketplace**: List used textbooks, cycle accessories, or electronics with price tags and image previews.
- **Maintenance & Complaints**: File room or campus infrastructure issues (Hostel, Academic, Mess, General) with live status tracking (`Under Review`, `In Progress`, `Resolved`).
- **Noticeboard**: Admin-managed announcement feed on the homepage for campus updates.
- **Admin Dashboard**: Full CRUD moderation and inline status updates via `/admin/`.

---

## Tech Stack

- **Backend**: Python 3.12+, Django 6.1
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3 (Custom Responsive Grid/Flexbox)
- **Image Processing**: Pillow

---

## Prerequisites & Installation

Make sure you have Git and Python installed on your machine before setting up the project.

### 1. Install Git & Python

- **macOS**:
    brew install git python

- **Ubuntu / Debian**:
    sudo apt update
    sudo apt install git python3 python3-venv python3-pip

- **Windows**:
  - Download and install Git from [git-scm.com](https://git-scm.com/).
  - Download Python 3.12+ from [python.org](https://www.python.org/) (ensure **"Add Python to PATH"** is checked during setup).

---

## Local Setup Guide

### 1. Clone the Repository
    git clone https://github.com/keyushtech/campus_buddy.git
    cd campus_buddy

### 2. Create and Activate Virtual Environment

- **macOS / Linux**:
    python3 -m venv venv
    source venv/bin/activate

- **Windows (Command Prompt)**:
    python -m venv venv
    venv\Scripts\activate

- **Windows (PowerShell)**:
    python -m venv venv
    .\venv\Scripts\Activate.ps1

### 3. Install Python Dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

*(If setting up manually without a requirements file: `pip install django pillow`)*

### 4. Database Setup & Admin Initialization
Run the initial database migrations to configure SQLite:
    python manage.py makemigrations
    python manage.py migrate

Create a superuser account to access the administrative dashboard:
    python manage.py createsuperuser

Follow the interactive prompts to set your username, email, and password.

### 5. Start the Development Server
    python manage.py runserver

Open your browser and navigate to:
- **Student Portal**: http://127.0.0.1:8000/
- **Admin Dashboard**: http://127.0.0.1:8000/admin/

---

## Team & Contribution Breakdown

| Contributor | Role | Module Coverage |
|---|---|---|
| **Keyush** | Lead / Architecture | Project scaffolding, core URL routing, settings, admin setup, announcement data models & dynamic home view |
| **Manohar** | UI/UX & Grievance Lead | Responsive design system, base layout, complaints module (models, views, forms, filters, and admin dashboard) |
| **Lavanya** | Module Lead (Lost & Found) | Lost & found data models, image upload handling, feeds, and post submission forms |
| **Vaishnavi** | Module Lead (Marketplace) | Marketplace listing models, image uploads, price displays, views, and routing |
