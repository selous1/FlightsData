# Deployment commands

This is a temp file for me to just put all commands I am using to deploy kubernetes

# Microservices

Starting minikube

```bash
minikube start
```

## Secrets

Add a secret, which consists of a JSON file with the project_id, private_key and other information needed for the microservices to access the BigQuery database.

```bash
kubectl create secret generic my-secret --from-literal "API_TOKEN=$(cat .secrets/cnproject-381016-3aa6da06c093.json)"
```

```bash
kubectl create secret generic aws-secret \
    --from-file=AWS_ACCESS_KEY_ID=.secrets/AWS_ACCESS_KEY_ID.txt \
    --from-file=AWS_ACCESS_KEY_SECRET=.secrets/AWS_ACCESS_KEY_SECRET.txt
```

```bash
kubectl create -f k8s/config-maps/config-map.yaml
```

Reference: <https://www.youtube.com/watch?v=cQAEK9PBY8U>

## Deploy Ingress

```bash
kubectl apply -f k8s/ingress/ingress-nginx.yml
```

```bash
kubectl apply -f k8s/ingress/ingress-resource.yml
```

## Deploy service account

```bash
kubectl apply -f k8s/roles/service-account.yaml
```

```bash
kubectl apply -f k8s/roles/airline_role.yaml
```

```bash
kubectl apply -f k8s/roles/airline_role_bind.yaml
```

## Deploy all microservices

```bash
kubectl apply -f k8s/deployments/
```

## Start Prometheus

Create monitoring namespace

```bash
kubectl apply -f k8s/monitoring/monitoring.yml
```

Create cluster role

```bash
kubectl create -f k8s/monitoring/cluster-role.yml
```

Deploy Prometheus

```bash
kubectl create -f k8s/monitoring/prometheus-config.yml

kubectl create -f k8s/monitoring/prometheus-deployment.yml

kubectl create -f k8s/monitoring/prometheus-service.yml
```

## Start Grafana

```bash
kubectl apply -f k8s/monitoring/grafana.yaml
```

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
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80
```

Test

```bash
curl localhost:8080/airlines/G4
```

```bash
kubectl exec -it POD-NAME -- /bin/bash
```

# RUn Grafana

```bash
kubectl port-forward service/grafana-svc 8081:3000
```

User/Password: admin/admin

Add data source -> Prometheus | Put url (nodeport: <http://192.168.49.2:30000> )
Create dashboard -> New Panel -> Select metric
