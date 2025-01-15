# RabbitMQ Django App Installation Guide

This guide provides step-by-step instructions to set up a Django project integrated with RabbitMQ.

## Prerequisites
- Python, Django and virtualenv Installed
- Docker and Docker Compose installed

## Installation Steps

### Step 1: Set Up a Virtual Environment

1. Create a virtual environment:
   ```bash
   virtualenv -p python3 env
   ```

2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Apply migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Step 3: Set Up RabbitMQ with Docker

1. Install Docker:
   - Follow the [Docker installation guide](https://docs.docker.com/engine/install/ubuntu/).
   - Perform the [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/).

2. Run RabbitMQ server:
   ```bash
   docker-compose up -d
   ```

3. Check RabbitMQ Management UI:
   - Visit `http://localhost:8080`.
   - Use `guest` as both the username and password.

### Step 4: Start the Development Server

1. Run the Django development server:
    ```bash
    python manage.py runserver
    ```
2. Run Consumer
   ```bash
   python manage.py run_consumer
   ```

## Conclusion
You have now successfully set up a Django project integrated with RabbitMQ for inventory management. RabbitMQ is running on Docker, and the consumer is managed through Django's custom management commands. Happy coding!

