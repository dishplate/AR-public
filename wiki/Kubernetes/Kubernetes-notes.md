# Kubernetes notes

## Setup
1. SSH into system with docker installed
2. Install Kind (Kuberntest in docker)
3. Install Kubectl

## Getting a cluster setup
## Create a single node cluster
kind create cluster --name my-first-kind
kubectl cluster-info --context kind-my-first-kind
## delete the cluster
kind delete cluster --name my-first-kind
### See what clusters are running
kind get clusters
### View the context
kubectl cluster-info --context kind-kind01
### View the nodes
kubectl get nodes
### Switch the context
kubectl config use-context kind-kind01. (kind- prefix is added automatically)

## create a cluster using a config file
kind create cluster --name my-first-kind --config config.yaml


