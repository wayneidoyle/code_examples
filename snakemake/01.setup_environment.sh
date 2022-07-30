#!/bin/bash
# Installs dependencies for running Snakemake
# Installation will require user input on the terminal (license response and installation decisions)

# Make and enter a folder for storing code install scripts
mkdir -p ~/code_installs
cd ~/code_installs

# Download and install Mambaforge
curl -L https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh -o Mambaforge-Linux-x86_64.sh
bash Mambaforge-Linux-x86_64.sh

# Reperform initialization so conda installation can take affect
source ~/.bashrc

# Set-up location for tutorials
mkdir -p ~/code_tutorials/snakemake_official
cd ~/code_tutorials/snakemake_official

# Download example workflow
curl -L https://github.com/snakemake/snakemake-tutorial-data/archive/v5.24.1.tar.gz -o snakemake-tutorial-data.tar.gz
tar --wildcards -xf snakemake-tutorial-data.tar.gz --strip 1 "*/data" "*/environment.yaml"
rm snakemake-tutorial-data.tar.gz

# Set-up conda environment
conda activate base
mamba env create --name snakemake-tutorial --file environment.yaml
conda activate snakemake-tutorial

# Confirm environment is set-up correctly by printing snakemake help
snakemake --help