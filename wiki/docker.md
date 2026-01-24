# Docker notes (Applies to Podman too)
## Installation
Follow the installation on docker's website

## Commands
https://docs.docker.com/reference/cli/docker/
- docker pull image name - This pulls an image from the default registry, docker hub. To pull from a different registry:

    docker image pull myregistry.local:5000/testing/test-image
    docker pull hello-world


## Notes
- Containers are run from an image
- An image can be used to create any number of containers
- Containers cannot be modified when they are running, if you need to store data, you have to map an external storage to the container as you would any Linux system.
