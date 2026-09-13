https://www.linkedin.com/learning/learning-kubernetes-16086900/spin-up-and-explore-a-minikube-cluster?resume=false&u=86813962

# Pods managed by a Deployment : deleting only the pod will cause Kubernetes to recreate it.
First identify its Deployment:
kubectl get deployments

Then stop it by scaling it to zero replicas:
kubectl scale deployment synergychat-web --replicas=0

# Deleting deployments
kubectl delete -f deployment.yml

# Check status of pods
kubectl get pods -A
-A all pods, not just the default namespace

# To launch a deployment with more or less replica containers
kubectl scale deployment synergychat-web --replicas=1

# Namespaces
kubectl get namespaces  [you can shorten it and use ns]

# Show running services (servicesact as loadbalancers)
kubectl get services -A
NAMESPACE     NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
default       kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP                  3d22h
kube-system   kube-dns     ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   3d22h

- Gitops course mentioned

### YAML, JSON and XML are data serialization languages, designed to be easily read by humans. ###
- 3 horizontal lines means it's the beginning of a yaml doc. You can use the # symbol is a note
- yaml stores key value pairs separated by a colon
- Yaml or yml can be used.
- Indentation is really easily to mess up, use ai or yaml checker.

---
# Deploying a namespace
Eg. separate pd and np using namespaces

kubectl get namespaces

# deploy a namespace from a yaml
kubectl apply -f namespace.yml
You can add separate namespaces in a single document by separating them with 3 dashes ---

# Delete namespaces via yaml/manifest?
kubectl delete -f namespace.yml

Pods are the kubernetes resources that run your micro services and resources
deployment.yml is a kubernetes spec for a deployment
kind:    this is the kind of kubernetes object to create

kubectl get deployments -A
kubectl get deployments -n development
kubectl get pods -n development
Delete a pod
kubectl delete pod pod-info-deployment-cf5db879-6tmrr -n development

# Logging
kubectl describe pod pod-info-deployment-cf5db879-jtjf5 -n development

# Busybox

## kubectl get pods -n development -o wide
-o shows us extra info about pods including ip addresses

# Show all pods regardless of namespace with IP addresses
kubectl get pods -A -o wide

# Getting into a pod
kubectl exec -it podname -- /bin/sh
the shell can vary

Having issues connecting from busybox shell to the other pods on port 3000. Port 80 works for the default nginx data.
wget 10.244.0.28:3000
Connecting to 10.244.0.28:3000 (10.244.0.28:3000)
wget: can't connect to remote host (10.244.0.28): Connection refused

