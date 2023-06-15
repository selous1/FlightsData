Blue='\033[0;34m'  
BGreen='\033[1;32m' 
BRed='\033[1;31m'
Plane='\U2708'
Saucer='\U1F6F8'
Rocket='\U1F680'
echo -e "${Rocket}${Blue}Starting Deployment of plane API ${Plane} ${Saucer}"

# Create Secret
ClosedBook='\U1F4D5'
echo -e "${ClosedBook}${Blue}Starting Secret"
kubectl create secret generic my-secret --from-literal "API_TOKEN=$(cat .secrets/cnproject-381016-3aa6da06c093.json)"
kubectl create secret generic aws-secret \
    --from-file=AWS_ACCESS_KEY_ID=.secrets/AWS_ACCESS_KEY_ID.txt \
    --from-file=AWS_ACCESS_KEY_SECRET=.secrets/AWS_ACCESS_KEY_SECRET.txt
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Create Secret finished"
else
    echo -e "${BRed} Failed to creating Secret"
fi

# Create Config map
Map='\U1F5FA'
echo -e "${Map}${Blue}Starting Config Map"
kubectl create -f k8s/config-maps/config-map.yaml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Create Config map finished"
else
    echo -e "${BRed} Failed to creating Config map"
fi

# Ingress
Walking='\U1F6B6'
echo -e "${Walking}${Blue}Starting Ingress"
kubectl apply -f k8s/ingress/ingress-nginx.yml
kubectl apply -f k8s/ingress/ingress-resource.yml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Ingress finished"
else
    echo -e "${BRed} Failed to creating Ingress"
fi

# Prometheus
Fire='\U1F525'
echo -e "${Fire}${Blue}Starting Prometheus"
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

#Grafana
BookMark='\U1F4D1'
echo -e "${BookMark}${Blue}Starting Grafana"
kubectl apply -f k8s/monitoring/grafana.yaml
if [ $? -eq 0 ]
then
    echo -e "${BGreen} Grafana finished"
else
    echo -e "${BRed} Failed to creating Grafana"
fi

# Service account and roles
Card='\U1F4B3'
echo -e "${Card}${Blue}Starting Service Account"
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
Factory='\U1F3ED'
echo -e "${Factory}${BPurple} Do ${BCyan}kubectl apply -f k8s/deployments/ ${BPurple}to deploy application "

# Emoji Reference
# https://www.prosettings.com/emoji-list/#1f6f8