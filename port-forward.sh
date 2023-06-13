#!/bin/bash

services=("admin-s" "airline-s" "ranking-s" "flight-s" "predict-s")

for service in "${services[@]}"
do
  kubectl port-forward service/"$service" 8080:5000 &
done

# Wait for all port forwarding processes to finish
wait
