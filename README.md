# Flask-Microservice-Template

## Usage

To use this application, you will need to have Docker and Docker Compose installed on your system. Once you have those installed, navigate to the `Application` directory and run the `run.sh` script. This will start all the services defined in the `docker-compose.yml` file.

Here are the step-by-step instructions for using this microservice architecture:

1. Make sure you have Docker and Docker Compose installed on your system. If you don't have them installed, you can download them from their respective websites.

2. Open a terminal or command prompt and navigate to the `Application` directory of this architecture.

3. Run the `run.sh` script by typing `sh run.sh` and pressing enter. This will start all the services defined in the `docker-compose.yml` file.

4. Once all the services are running, you can interact with them using their respective APIs.

## Architecture

This architecture consists of several microservices: **auth**, **booking**, and **main**. Each of these microservices has its own **Dockerfile**, which is used to build a Docker image for that service. The services also have their own directories named **app** that contain the Python files `__init__.py` and `views.py`. Additionally, each service has a `requirements.txt` file that specifies its dependencies and a `run.py` file that starts the service.

The different services are orchestrated together using a `docker-compose.yml` file in the Application directory.
