#!/bin/bash

env_path=$HOME/mambaforge

RED='\033[0;31m'
GREEN='\033[0;32m' # Green
BLUE='\033[0;34m'  # Blue
NC='\033[0m' # No Color

# * Install rustup, this command is idempotent, if it's installed, it will just try to update.
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

if [ -f dataset/dataset.parquet ]; then
    echo -e "${RED}Dataset already exists, skipping download.${NC}"
else
    echo -e "${BLUE}Downloading dataset...${NC}"
    wget -O dataset/dataset.parquet 'https://ulisboa-my.sharepoint.com/:u:/g/personal/fc55312_alunos_fc_ul_pt/ET70WH8nOgRFoYGIPErr3TIBYGwFMwNguqUnUTRyizo3rw?e=9Kyvlt&download=1'
    echo -e "${GREEN}Dataset downloaded.${NC}"
fi

if [ -x "$(command -v mamba)" ]; then
    echo -e "${RED}Since mamba is installed, lets just update the environment!${NC}"
    
    mamba env update --name cen16-dev --file .config/envs/dev-conda-env.yml 1>&1 2>&2

    echo -e "${BLUE}Lets just have ansible do its thing!${NC}"
    bash .config/scripts/run-ansible.sh

    echo -e "${RED}Done, we can go on to deployment.${NC}"
    exit 1
fi

echo -e "${RED}Mamba command is not available, the script will proceed with it s instalation:${NC}"

if ! [ -f .config/scripts/mambaforge-install-script.sh ]; then
    echo 'The install script will be downloaded now'

    wget --no-check-certificate https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh \
        -O .config/scripts/mambaforge-install-script.sh

    echo -e "${GREEN}Install script downloaded.${NC}"
fi 

echo -e "${BLUE}we will now proceed with the installation:${NC}"

bash .config/scripts/mambaforge-install-script.sh -b

echo -e "${GREEN}mamba is now installed, the script will create the dev environment for you:${NC}"

export PATH=$env_path/condabin:$PATH

mamba env create -f .config/envs/dev-conda-env.yml

bash -c "$env_path/condabin/mamba init"
bash -c "$env_path/condabin/conda config --set auto_activate_base false"

echo -e "${BLUE}Lets just have ansible do its thing!${NC}"
bash .config/scripts/run-ansible.sh

cargo install drill

exec bash