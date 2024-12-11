# WEBHOOK.PY


## Description
This is a simple Dockerfile that creates a Docker image for a Flask Webhook API. The container runs an HTTP server on port 5000.

## Project Links
- **Docker Hub Repository**: [estebanandres/flask-webhook-app on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/flask-webhook-app/general)

## Getting Started

### Cloning the Repository
To clone the repository, use the following command:
```bash
git clone https://github.com/EstebanASM/WEBHOOK.PY.git
```
Navigate to the project directory:
```bash
cd WEBHOOK.PY
```

### Running the Application Locally (Without Docker)
#### Prerequisites
- Ensure[Python](https://www.python.org/downloads/) is installed on your machine.

- Install Flask and other necessary dependencies. You can do this by running:
   ```bash
   pip install -r requirements.txt

   ```

#### Running the Application
1. Inside the project directory, start the Flask server with:
   ```bash
   python webhook.py

   ```
2. Open your browser and go to:
   ```
   http://localhost:5000/webhook/data
   
   ```
3. Test your Webhook API endpoints as defined in the webhook.py file.

### Running the Application with Docker

To run the application with Docker, visit the Docker Hub repository for this project: [estebanandres/flask-webhook-app on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/flask-webhook-app/general)