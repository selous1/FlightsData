# Notes on creating a _decently_ robust script to install mambaforge:


## What we need to do:
1. Check if mamba is already installed and,
   1. If it is, skip installation
   2. If it's not, install it
2. Check if there is a "cen16-dev" environment
   1. If it exists, delete it
   2. If it does not, skip this step
3. Create the environment with the yml file

Fortunately, the install script for mamba checks if the program is already installed :).

Not only that the `update` method in conda/mamba will verify if the environment already exists and act accordingly. Not only that it also has the added bonus of updating the env with new packages if the yml file changes.
```sh
mamba env update -n cen16-dev -f .config/envs/dev-conda-env.yml
```

To install mamba in a brand new system you would do:
```sh
wget --no-check-certificate https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
chmod +x Mambaforge-Linux-x86_64.sh
./Mambaforge-Linux-x86_64.sh -b
.~/mambaforge/condabin/mamba init
exec bash
conda config --set auto_activate_base false
exec bash
mamba env create -f dev.yml
conda activate cen16-dev
```

## Results

In the end the script turned to:
```sh
#!/bin/bash

env_path=$HOME/mambaforge

RED='\033[0;31m'
GREEN='\033[0;32m' # Green
BLUE='\033[0;34m'  # Blue
NC='\033[0m' # No Color

if [ -x "$(command -v mamba)" ]; then
    echo -e "${RED}Since mamba is installed, lets just update the environment!${NC}"
    
    mamba env update --name cen16-dev --file .config/envs/dev-conda-env.yml 1>&1 2>&2

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

exec bash 
```

### Links:

1. https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default
2. https://github.com/conda-forge/miniforge#mambaforge
3. https://mamba.readthedocs.io/en/latest/installation.html
4. https://medium.com/@bluxmit/docker-as-a-lightweight-vm-docker-image-that-you-can-use-as-vm-substitute-164032e4ed0b
5. https://gist.github.com/jwebcat/5122366
6. https://stackoverflow.com/questions/42352841/how-to-update-an-existing-conda-environment-with-a-yml-file
7. https://gist.github.com/mlgill/3559ca9de860624f49b3
8. https://stackoverflow.com/questions/13799789/expansion-of-variables-inside-single-quotes-in-a-command-in-bash
9. https://stackoverflow.com/questions/30642021/stdout-and-stderr-redirection-in-child-process
10. https://stackoverflow.com/questions/592620/how-can-i-check-if-a-program-exists-from-a-bash-script
11. https://www.tutorialspoint.com/negate-an-if-condition-in-a-bash-script-in-linux
12. https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux