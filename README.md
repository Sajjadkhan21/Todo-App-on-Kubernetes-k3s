# Todo App on Kubernetes (k3s)

A simple Todo application deployed on a local Kubernetes (k3s) cluster using Docker, Flask, Redis, Nginx, and Traefik Ingress.

## Technologies Used

- **Python Flask** – Backend API
- **Redis** – Database for storing todos
- **HTML & JavaScript** – Frontend
- **Nginx** – Frontend web server
- **Docker** – Building container images
- **Kubernetes (k3s)** – Container orchestration
- **Traefik** – Ingress controller

## Project Structure

```text
todo-app/
├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
└── k8s/
    ├── redis.yaml
    ├── api.yaml
    ├── frontend.yaml
    └── ingress.yaml
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sajjadkhan21/Todo-App-on-Kubernetes-k3s.git
```

### 2. Navigate to the Project Directory

```bash
cd Todo-App-on-Kubernetes-k3s
```

### 3. Build Docker Images

Build the backend API image:

```bash
docker build -t todo-api:v1 ./api
```

Build the frontend image:

```bash
docker build -t todo-frontend:v1 ./frontend
```

### 4. Import Images into k3s

Import the API image:

```bash
docker save todo-api:v1 | sudo k3s ctr images import -
```

Import the frontend image:

```bash
docker save todo-frontend:v1 | sudo k3s ctr images import -
```

Verify the images:

```bash
sudo k3s ctr images ls | grep todo
```

### 5. Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

### 6. Check Pods

```bash
kubectl get pods
```

Wait until all pods are running.

### 7. Access the Application

Open the following URL in your browser:

```text
http://localhost
```

## Features

- Add new todo tasks.
- View all todo tasks.
- Mark tasks as completed or incomplete.
- Delete todo tasks.
- Store todo data in Redis.
- Run multiple API and frontend replicas using Kubernetes.

## Learning Objectives

- Docker image creation and management.
- Deploying applications on Kubernetes (k3s).
- Working with Pods, Deployments, and Services.
- Configuring Kubernetes Ingress with Traefik.
- Connecting Flask applications with Redis.
- Scaling deployments and performing rolling updates.
- Understanding container orchestration and microservices.

## Author

Sajjad Ullah

## GitHub Repository

[Todo App on Kubernetes (k3s)](https://github.com/Sajjadkhan21/Todo-App-on-Kubernetes-k3s)
