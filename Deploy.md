# Deployment commands dump

This is a temp file for me to just put all commands I am using to deploy kubernetes

# Microservices

Starting minikube

```bash
minikube start
```

Adding secret to environment variables, by putting the cat of the JSON key in the variable

```bash
kubectl create secret generic my-secret --from-literal "API_TOKEN=$(cat .secrets/cnproject-381016-3aa6da06c093.json)"
```

Remove secret from kubectl

kubectl delete secret my-secret


Reference

https://www.youtube.com/watch?v=cQAEK9PBY8U

## Deploy Ingress

```bash
kubectl apply -f .config/ingress/
```

## Deploy Logging

```bash
kubectl apply -f .config/logging/
```

## Deploy all microservices

```bash
kubectl apply -f deploy/
```

# Remove Microservices

## Remove all services

```bash
kubectl delete --all services
```

## Remove all deployments

```bash
kubectl delete --all deployment
```

## Alternative to remove everything

```bash
kubectl delete all --all
```

# Aditionals

Get everything in kubectl

```bash
kubectl get all
```

Run a command in a specific pod (sh if we want to access the pod shell)

```bash
kubectl exec -it "pod-name" "command"
```

Check the std out of the pod when it crashed 

```bash
kubectl logs pod-name
```

Port forward to send message to nginx from localhost

```bash
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 9000:80
```
