FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/dev-conda-env.yml /app

RUN mamba env create -f dev-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

# Set the pull policy to always for Conda
RUN mamba config --set remote_read_timeout_secs 600
RUN mamba config --set channel_priority strict
RUN conda config --set update_modifier always

SHELL ["conda", "run", "-n", "cen16-dev", "/bin/bash", "-c"]

COPY ./src/flights /app

# Copy grpc
COPY ./src/GRPC /app/GRPC

EXPOSE 5000

ENTRYPOINT ["conda", "run", "--no-capture-output", "--pull", "always", "-n", "cen16", "python", "microservice/app.py"]