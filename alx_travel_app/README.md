# AlxTravelApp

Backend system for **ALX Travel App** built with Django, Celery, and MySQL.  
This project demonstrates asynchronous task processing, database integration, and production-ready configurations for scalable backend services.

---

## 🚀 Features

- **Django 5+** as the core web framework
- **MySQL** database for persistence
- **Celery + RabbitMQ (AMQP/rpc)** for asynchronous task processing
- **Swagger (drf-yasg)** for API documentation
- **CORS support** for frontend integration
- Modular app structure for scalability

---

## 📂 Project Structure

```bash

alx_travel_app/
│── manage.py
│── requirements.txt
│── README.md
│
├── alx_travel_app/ # Main Django project
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── celery.py # Celery configuration
│ ├── asgi.py
│ └── wsgi.py
│
├── listings/ # Listings Django app
│ ├── models.py
│ ├── views.py
│ ├── tasks.py # Celery tasks
│ └── ...

```

---

## ⚙️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/mnswifi/alx_travel_app.git
cd alx_travel_app
```

### 2. Create & activate virtual environment

```bash
python3 -m venv alxenv
source alxenv/bin/activate
```

### 3. Install dependencies

Make sure system packages for MySQL are installed:

```bash
sudo apt update
sudo apt install -y default-libmysqlclient-dev build-essential pkg-config python3-dev
```

Then install Python requirements:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a .env file in the project root:

```bash
DEBUG=True
SECRET_KEY=your-secret-key

# MySQL
DATABASE_NAME=alx_travel
DATABASE_USER=dbuser
DATABASE_PASSWORD=dbpassword
DATABASE_HOST=localhost
DATABASE_PORT=3306

# Celery with RabbitMQ
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
CELERY_RESULT_BACKEND=rpc://

```

Update settings.py to load environment variables (e.g. with django-environ).

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start development server

```bash
python manage.py runserver
```

📌 Celery Setup

### 1. Start RabbitMQ

Make sure RabbitMQ is installed and running:

```bash
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
```

### 2. Start Celery worker

```bash
celery -A alx_travel_app worker -l info
```

### 3. (Optional) Start Celery Beat for periodic tasks

```bash
celery -A alx_travel_app beat -l info
```

📖 API Documentation

Swagger docs available at:

```bash
http://127.0.0.1:8000/swagger/
```

🧪 Running Tests

```bash
python manage.py test
```
