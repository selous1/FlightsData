#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m' # Green
BLUE='\033[0;34m'  # Blue
NC='\033[0m' # No Color

source ${HOME}/mambaforge/etc/profile.d/conda.sh

# ? activate mamba env in this bash shell
conda activate cen16-dev

# * After getting the mamba env activated:
ansible-galaxy install -r .config/envs/ansible-requirements.yml # this command is idempotent

echo -e "${BLUE}The ansible playbook will ask for you password. Please input it when asked in BECOME password${NC}"
ansible-playbook -K .config/playbooks/depencies-playbook.yaml

exit 0