# airlines
docker run -p 5004:5000 -d \
-e TABLE_NAME='cnproject-381016.flights_data.dataset' \
-e API_TOKEN="$(cat .secrets/cnproject-381016-3aa6da06c093.json)" \
--name airlines therobertsan/airline-container:v2
# 370

# admin
docker run -p 5003:5000 -d \
-e TABLE_NAME='cnproject-381016.flights_data.dataset' \
-e API_TOKEN="$(cat .secrets/cnproject-381016-3aa6da06c093.json)" \
--name admin santig007/cnproject:admin1.0
# 320

# ranking
docker run -p 5002:5000 -d \
-e TABLE_NAME='cnproject-381016.flights_data.dataset' \
-e API_TOKEN="$(cat .secrets/cnproject-381016-3aa6da06c093.json)" \
--name ranking selous1/ranking:v1.5
# 260

# flights
docker run -p 5001:5000 -d \
-e TABLE_NAME='cnproject-381016.flights_data.dataset' \
-e API_TOKEN="$(cat .secrets/cnproject-381016-3aa6da06c093.json)" \
--name flights selous1/flights:v1.0
# 290Mb  

# prediction
docker run -p 5000:5000 -d -e AWS_ACCESS_KEY_ID="$(cat .secrets/AWS_ACCESS_KEY_ID.txt)" \
-e AWS_ACCESS_KEY_SECRET="$(cat .secrets/AWS_ACCESS_KEY_SECRET.txt)" \
-e AWS_REGION='eu-north-1' \
-e AWS_FUNCTION_NAME='arn:aws:lambda:eu-north-1:621272430898:function:testfunction' \
--name pred prediction:latest
# 5Mb
