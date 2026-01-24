# Docker notes (Applies to Podman too)
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
## Running containters
- docker run -d hello-world. This runs in detached mode. Your terminal is free to do other things.
- docker ps -a (list all containers, even ones not running)
- docker stop "container ID" or name of container
- docker remove "container ID". Removes the container.
- docker exec -it <container ID> /bin/bash 


## Notes
- Containers are run from an image
- An image can be used to create any number of containers
- Containers cannot be modified when they are running, if you need to store data, you have to map an external storage to the container as you would any Linux system.
