#!/bin/bash

env_path=$HOME/mambaforge

RED='\033[0;31m'
GREEN='\033[0;32m' # Green
BLUE='\033[0;34m'  # Blue
NC='\033[0m' # No Color

if [ ! -x "$(command -v cargo)" ]; then
    echo -e "${RED}Since cargo is not available, lets install rustup${NC}"

    exit 0
fi

echo -e "${RED}rust is installed${NC}"

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y