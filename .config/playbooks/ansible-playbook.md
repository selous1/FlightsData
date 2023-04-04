# Notes on creating the ansible playbook

## terraform (& docker & minikube & kubectl, for that matter):
The recommended terraform installation is not as simple as `apt install terraform`, the repo has to be "installed".
This means that regular ansible roles for system packages will not do the job.
Fortunately there are some roles in galaxy that do this exact job. 

This means that I will have to find some roles to do these, off to ansible-galaxy.

## rust:
I didn't find, any rustup roles that worked... I tried about 5 but they all hung up on some detail or another with no documentation,
Fortunately, the rustup sh file is already idempotent, so lets just use sh for that...

### installing the required roles
ansible-galaxy install -r requirements.yml

### Links
1. https://stackoverflow.com/questions/25230376/how-to-automatically-install-ansible-galaxy-roles
2. https://github.com/ansible/ansible/issues/35645
3. https://galaxy.ansible.com/geerlingguy/docker

### Random notes: 
professor expects (cpu and memory) requests and limits for the work (29/03)