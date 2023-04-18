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

## Admin

```bash
kubectl apply -f src/admin/admin-dep.yaml
kubectl describe deploy admin-d
```



## Ingress

```bash
kubectl apply -f ingress-nginx.yml
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=120
kubectl apply -f ingress-resource.yml
```

For local testing

``` bash
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80
```

## Prometheus Server

```bash
kubectl create configmap prometheus-cm --from-file prometheus-cm.yaml
kubectl apply -f prometheus.yaml
```