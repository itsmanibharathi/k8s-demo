# Frontend Setup

To set up and run the frontend container, I followed these steps:

## 1. Build and Run the Frontend

First, I ran the following command to build the Docker image for the frontend and start the container:

```bash
docker build -t frontend . && \
docker run -d -p 8080:80 --name frontend frontend
