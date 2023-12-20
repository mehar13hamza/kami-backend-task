# Kami Backend Developer Task

## Prerequisites

Install Docker Desktop for running this project, instructions are found here:
https://docs.docker.com/desktop/

## Build Containers

Run following command to build the containers:

```
make build
```

## Run Containers

```
make up
```

## Stop and delete containers

```
make down
```

## Run tests

```
make tests
```

## For looking at test coverage

```
make coverage-report
```

## Start Project

After building and running containers visit this url to access the APIs of this project.

```
http://localhost:8000/swagger/
```
