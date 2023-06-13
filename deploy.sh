Blue='\033[0;34m'  
BGreen='\033[1;32m' 
BRed='\033[1;31m'
echo -e "${Blue}Starting Deployment"

# Create Secret
kubectl create secret generic my-secret --from-literal "API_TOKEN=$(cat .secrets/cnproject-381016-3aa6da06c093.json)"
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Create Secret finished"
else
    echo -e "${BRed} Failed to creating Secret"
fi

# Create Config map
kubectl create -f k8s/config-maps/config-map.yaml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Create Config map finished"
else
    echo -e "${BRed} Failed to creating Config map"
fi

# Ingress
kubectl apply -f k8s/ingress/ingress-nginx.yml
kubectl apply -f k8s/ingress/ingress-resource.yml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Ingress finished"
else
    echo -e "${BRed} Failed to creating Ingress"
fi

# Prometheus
kubectl apply -f k8s/monitoring/monitoring.yml
kubectl create -f k8s/monitoring/cluster-role.yml
kubectl create -f k8s/monitoring/prometheus-config.yml
kubectl create -f k8s/monitoring/prometheus-deployment.yml
kubectl create -f k8s/monitoring/prometheus-service.yml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Prometheus finished"
else
    echo -e "${BRed} Failed to creating Prometheus"
fi

# Service account and roles
kubectl apply -f k8s/roles/service-account.yaml
kubectl apply -f k8s/roles/airline_role.yaml
kubectl apply -f k8s/roles/airline_role_bind.yaml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Service account and roles finished"
else
    echo -e "${BRed} Failed to creating Service account and roles"
fi

# Deployment
# kubectl apply -f k8s/deployments/
# if [ $? -eq 0 ]
# then
#     echo -e "${BGreen} Deployment finished"
# else
#     echo -e "${BRed} Failed to creating Deployment"
# fi
BPurple='\033[1;35m'
BCyan='\033[1;36m'
echo -e " ${BPurple} Do ${BCyan}kubectl apply -f k8s/deployments/ ${BPurple}to deploy application "