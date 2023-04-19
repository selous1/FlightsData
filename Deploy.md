# Deployment commands dump

This is a temp file for me to just put all commands I am using to deploy kubernetes

# Microservices

Starting minikube

```bash
minikube start
```

Adding secret to environment variables

```bash
kubectl create secret generic my-secret --from-file=cert=.secrets/cnproject-381016-3aa6da06c093.json
```

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

```bash
kubectl delete all --all
```

```bash
kubectl get all
```

```bash
kubectl exec -it pod-name sh
```