# Kubernetes notes

## Setup
1. SSH into system with docker installed
2. Install Kind (Kuberntest in docker)
3. Install Kubectl

## Getting a cluster setup
### Start a cluster
kind create cluseter --name=kind01
### See what clusters are running
kind get clusters
### View the context
kubectl cluster-info --context kind-kind01
### View the nodes
kubectl get nodes
### Switch the context
kubectl config use-context kind-kind01. (kind- prefix is added automatically)
