# Docker in Docker Demo

## Volume mount issue
In a DinD setup, a regular directory mount does not work so we need to create an external volume first before we can share content between a child and parent container. See the following code snippet -
```bash 
docker create volume shared_vol
docker run --name service_A -v shared_vol:/app/shared
```
Then share the volume with the child container - 
```Python
        result = subprocess.run([
            "docker", "run", "--rm",
            "-v", "shared_vol:/app",
            "--name", "container-c",
            "python:3.9-alpine",
            "python", "/app/main.py"
```

## Docker compose
A docker compose can automate the communication complications but the shared docker volume will need to be mnaged externally.