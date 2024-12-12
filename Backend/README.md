# Backend Setup

To set up and run the backend container, I followed these steps:

## 1. Build and Run the Backend

First, I ran the following command to build the Docker image for the backend and start the container:

```bash
docker build -t backend . && \
docker run -d -p 6001:6001 --name backend --link database:database backend
