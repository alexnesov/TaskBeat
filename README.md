# TaskBeat
Dynamic task management with Celery, RabbitMQ, FastAPI, Redis, and Docker. Real-time monitoring, scheduling, and advanced queuing for efficient task orchestration

System built using Python, Celery, RabbitMQ, FastAPI, Redis, and Docker. This project provides a scalable and efficient solution for handling asynchronous tasks with ease.

## Key Features:

- Asynchronous Task Processing: Leveraging Celery and RabbitMQ, TaskBeat allows for the efficient execution of tasks asynchronously, enabling improved performance and scalability.
- API with FastAPI: Built with FastAPI, TaskBeat offers a robust RESTful API for seamless integration and interaction with the task management system.
- Persistent Storage with Redis: Task statuses and other essential data are stored and managed using Redis, ensuring reliability and persistence.
- Containerized Deployment with Docker: TaskBeat is packaged as Docker containers, facilitating easy deployment and management across different environments.

## Usage:

- Submit tasks through the intuitive FastAPI endpoints.
- Monitor task statuses and retrieve results effortlessly.
- Scale and manage the task processing infrastructure efficiently with Celery and RabbitMQ.
- Deploy TaskBeat seamlessly using Docker, ensuring consistency and reliability across environments

## How to use it:

- git clone the repo
- at the ```root``` of the project, ```docker compose up```
- To play with the api, access: ```http://0.0.0.0:8000/docs```
- To access RabbitMQ: ```http://localhost:15672/```


## General useful commands:


To stop all containers and remove them:

- ```docker stop $(docker ps -aq) && docker rm $(docker ps -aq)```

To stop all celery processes:
- ```ps aux | grep celery | awk '{print $2}' | xargs kill```

```
.
└── Taskbeat/
    ├── app/
    │   ├── __init__.py
    │   ├── celery_worker.py
    │   ├── dependencies.py
    │   ├── main.py
    │   ├── models.py
    │   └── utils.py
    ├── docker-compose.yml
    ├── Dockerfile
    └── requirements.txt
```



- docker run --name my-redis-container -d -p 6379:6379 redis
- docker pull rabbitmq:management
- docker run -d --name my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:management
