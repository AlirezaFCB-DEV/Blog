# Django Practice Project – Blog & Accounts

> **A single-app Django project built for learning and mastering core concepts.**  
> No templates, no tests, no debugging – pure **development practice**.

---

## Overview

This is a **learning-focused** Django project containing **one Django app** (`blog`) that includes an `accounts` section with a **custom user model**. The goal is **hands-on development** – not production readiness.

- **Frontend**: Handled entirely in **React** (or any JS framework) → **No Django templates** are used.  
- **Backend**: Pure Django – API-ready, modular, and extensible.  
- **Purpose**: Master 13 professional Django topics **project-first** while building a real blog.


---

## Key Features (So Far)

- Custom User model (`CustomUser`) with **email-based authentication**
- `AUTH_USER_MODEL = 'accounts.CustomUser'` set in `settings.py`
- Basic blog post model with author relationship
- Ready for **API-first** development (DRF later)

---

## Tech Stack

| Layer        | Technology                     |
|-------------|--------------------------------|
| Backend     | Django (latest)                |
| Auth        | Custom User + Django auth      |
| Frontend    | **React** (or Vue/Any) – SSR   |
| Database    | SQLite (dev) → PostgreSQL (prod)|
| Deployment  | Gunicorn / Uvicorn (later)     |

---

## 13 Core Django Topics Covered (Project-Based)

| # | Topic                          | Docs |
|---|-------------------------------|------|
| 1 | **Custom User Model**          | [link](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/) |
| 2 | **Authentication & Authorization** | [link](https://docs.djangoproject.com/en/5.0/topics/auth/default/) |
| 3 | **Middlewares**                | [link](https://docs.djangoproject.com/en/5.0/topics/http/middleware/) |
| 4 | **Signals**                    | [link](https://docs.djangoproject.com/en/5.0/topics/signals/) |
| 5 | **Custom Managers & QuerySets**| [link](https://docs.djangoproject.com/en/5.0/topics/db/managers/) |
| 6 | **Forms & ModelForms**         | [link](https://docs.djangoproject.com/en/5.0/topics/forms/) |
| 7 | **Template Inheritance** *(skipped – React handles UI)* | — |
| 8 | **Context Processors** *(optional)* | [link](https://docs.djangoproject.com/en/5.0/ref/templates/api/#writing-your-own-context-processors) |
| 9 | **Static & Media Files**       | [link](https://docs.djangoproject.com/en/5.0/topics/files/) |
|10 | **Class-Based Views (Advanced)**| [link](https://docs.djangoproject.com/en/5.0/topics/class-based-views/) |
|11 | **Pagination**                 | [link](https://docs.djangoproject.com/en/5.0/topics/pagination/) |
|12 | **Caching**                    | [link](https://docs.djangoproject.com/en/5.0/topics/cache/) |
|13 | **Deployment Checklist**       | [link](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/) |

> **We continue from Topic 2 onward – building on the existing blog app.**

---

## Development Rules

- **No Django templates** → React handles rendering (SSR/CSR)
- **All logic stays in Django** → Clean, reusable, API-ready
- **Project-first learning** → Every topic = real feature
- **No tests yet** → Focus is **understanding & building**

---

## How to Run

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# 2. Install dependencies
pip install django

# 3. Run migrations
python manage.py migrate

# 4. Create superuser
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
