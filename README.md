# proj-cn-16

# Cloning this repository

To clone this project you can run:
```
git clone git@github.com:selous1/proj-cn-16.git --branch v0.0.3
```

## Requirements

*TO DO SH FILE*
(idea: create an ansible role that install all requirements,
with this the sh script would only be responsible for installing ansible and then running the playbook)

1. Local Kubernetes env (kind or minikube?) 
2. Ansible
3. Terraform
4. 

We provide a shell script and an ansible playbook to install all of these requirements, to run it you just need to run:
```sh
./install-requirements.sh
```

## Project Setup with VSCode

This project already contains a .vscode folder containing the recommended extensions and their configurations and so this is the preferred editor to view/use and run this project.

After cloning the repo open the main folder of this project and vscode will prompt you to install the necessary extensions if you don't have all of them already.

## Local and Cloud Deployments

We make use of local kubernetes environments so that developers can test their changes locally (saving time, reducing complexity and managing the limited cloud credits) and then deploy to the cloud.
This Local Deployment is powered by (#TODO find the best local k8s engine) that is also installed with the other requirements.

[//]: # (Internal note: I(j) thought that minikube was only vm based, so it was slower than kind, but the professor corrected me and explained that it is no longer the case. For that reason my vote goes to minikube because that is what is going to be used in the TP classes)

### Local Deploy

(#TODO save here the commands for local deployment)

### Cloud Deploy

(#TODO save here the commands for cloud deployment)

## Running the application

