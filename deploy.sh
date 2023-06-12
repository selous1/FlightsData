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
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.6.4/deploy/static/provider/cloud/deploy.yaml
kubectl apply -f k8s/ingress/ingress-resource.yml
while [ $? -lt 0 ]; do
   kubectl apply -f k8s/ingress/ingress-resource.yml
   sleep 10
done

if [ $? -eq 0 ]
then
    echo -e "${BGreen} Ingress finished"
else
    echo -e "${BRed} Failed to creating Ingress"
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
echo -e " ${BPurple} Do ${BCyan}kubectl apply -f k8s/deployments/ ${BPurple}to deploy application