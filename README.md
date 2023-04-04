# proj-cn-16

# Cloning this repository

To clone this project you can run:
```
git clone git@github.com:selous1/proj-cn-16.git --branch v0.0.3
```

## Project Setup:

To install both development and deployment requirements for this project a script has been included:

To install the dependencies run these commands from the root of the project:
```sh
chmod +x install-dependencies.sh
./install-dependencies
```

This script checks to see if the command `mamba` is available in your `$PATH`, if it's not then [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) (the recommended distribution of [mamba](https://github.com/mamba-org/mamba)) will be installed and the development environment will be created automatically.
Then the job of actually installing the other software safely is in the hands of [ansible](https://www.ansible.com/) that is installed in the dev mamba env.
Ansible then installs:
1. [Terraform](https://www.terraform.io/)
2. [Minikube](https://github.com/kubernetes/minikube)
3. [Kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/)
4. [Rustup](https://rustup.rs/)

### Project Setup with VSCode

This project already contains a .vscode folder containing the recommended extensions and their configurations and so this is the preferred editor to view/use and run this project.

After cloning the repo open the main folder of this project and vscode will prompt you to install the necessary extensions if you don't have all of them already.

## Local and Cloud Deployments

We make use of local kubernetes environments so that developers can test their changes locally (saving time, reducing complexity and managing the limited cloud credits) and then deploy to the cloud.
This Local Deployment is powered by (#TODO find the best local k8s engine) that is also installed with the other requirements.

[//]: # (Internal note: I(j) thought that minikube was only vm based, so it was slower than kind, but the professor corrected me and explained that it is no longer the case. For that reason my vote goes to minikube because that is what is going to be used in the TP classes)

### Local Deploy

(#TODO save here the commands for local deployment)

### Cloud Deploy

Create flight deployment and service that can be accessed from outside the cluster.
```
kubectl apply -f flight-dep.yaml
```
Create airline deployment and service that can be accessed from outside the cluster.
```
kubectl apply -f airline-dep.yaml
```
To test, run:
```
curl -4 CLUSTER-IP:3000/
```
You should receive an OK message

Keys have not yet been added to a Secret Resource, and are located inside the container.

## Running the application

