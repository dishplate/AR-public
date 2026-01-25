# Docker notes (Applies to Podman too)

## Quick Dockerfile config
FROM nginx
WORKDIR /app
COPY COPY ./index.html /usr/share/nginx/html/index.html #nginx default page modification


## Installation
Follow the installation on docker's website

## Commands
https://docs.docker.com/reference/cli/docker/
## Images
- docker pull "image name" - This pulls an image from the default registry, docker hub. To pull from a different registry:

- docker image pull myregistry.local:5000/testing/test-image
- docker pull hello-world
- docker images. Shows images. You can use wildcards to help search for what you need.
    - docker images h*
- docker rmi. Deletes images.
## Running containers
- docker run -d hello-world. This runs in detached mode. Your terminal is free to do other things.
- docker ps -a (list all containers, even ones not running)
- docker stop "container ID" or name of container
- docker remove "container ID". Removes the container.
- docker exec -it "container ID" /bin/bash 
- docker build -t my-nginx .  #Dockerfile in the current directory
- docker run -d -p 80:80 my-nginx:latest 

## Notes
- A container is a runtime instance of an image.
    - You can have two isolated containers derived from the same image, eg. dev and prod.
    - They are epemeral, portable and isolated.
- An image can be used to create any number of containers
    - Images are immutable
- Containers cannot be modified when they are running, if you need to store data, you have to map an external storage to the container as you would any Linux system.

## Docker file
 - run - happens at build time (to the image)
 - CMD - happens at container runtime (to the container)

