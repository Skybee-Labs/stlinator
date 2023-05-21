# VS Code Dockerized Setup

## Prerequisites:
- Docker.
- Docker Compose.
- VS Code

## Install:
- Clone the repo to your local.
- In the root directory of the project, run:
    ```bash
    > docker-compose up -d
    > code .
    ```
- Once VS Code is up:
    - Click on the green button at the bottom left corrner,  and choose `Reopen in Container`
    - This will reload VS Code in the container
- Open a terminal in the new vscode window and it will drop you inside the container
    - `cd src`
    - `pipenv install`
    - `pipenv shell`

## Install new python dependencies:
While the container is up:
```bash
> docker exec -it -u 0 lambda-dev bash
```
Then inside the container:
```bash
> pipenv install <library name> --system
```

# Building the ARM64 Lambda Image and Container
Optionally you can run `docker-compose -f docker-compose-arm64.yml up --build -d` which will build the arm64 version of the lambda and spawn a running container.

Manually:
1. Build the base image:
    `docker build -t audio-extractor-lambda-base -f Dockerfile.base.arm64 .`
2. Build the lambda image:
    `docker build -t audio-extractor-lambda -f Dockerfile.arm64 .`
3. Spawn a container:
    `docker run -it --name extractor-lambda audio-extractor-lambda`