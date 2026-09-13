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

# 9/13/2026 Issue with port 3000 
``` 
not working was fixed by copilot by adding this below, the volume mount part was explained by copilot
   volumeMounts:
        - name: nginx-config
          mountPath: /etc/nginx/conf.d/default.conf
          subPath: default.conf
      volumes:
      - name: nginx-config
        configMap:
          name: nginx-config
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
  namespace: development
data:
  default.conf: |
    server {
        listen 3000;
        location / {
            root   /usr/share/nginx/html;
            index  index.html;
        }
    }
```
# Explanation for above
Maybe a difference in the couse material and the version of things I am using
Because containerPort is just metadata — it doesn't tell the process what port to listen on.

containerPort: 3000 only documents/exposes a port for Kubernetes networking (so other things like Service definitions or kubectl describe can reference it). It has zero effect on the actual nginx process inside the container.
What actually determines the port nginx binds to is its config file, /etc/nginx/conf.d/default.conf, which contains a listen directive. The stock nginx:stable-alpine3.24 image ships with listen 80; baked into that file.
So even though you declared containerPort: 3000, nginx itself never learned to listen on 3000 — it kept listening on 80 (which is why your original wget :80 worked and :3000 was refused).
The volumeMounts/volumes combo is what actually overwrites that default config file with your custom one (listen 3000;) at container start, so nginx reads the new directive and binds to 3000 for real. Without mounting it, the ConfigMap existed in the cluster but was never wired into the container's filesystem, so it had no effect.