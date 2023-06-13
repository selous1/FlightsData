FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/dev-conda-env.yml /app

RUN mamba env create -f dev-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

SHELL ["conda", "run", "-n", "cen16-dev", "/bin/bash", "-c"]

COPY ./src/flights /app
COPY ./src/GRPC /app

EXPOSE 5003
EXPOSE 50051

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cen16-dev", "python", "app.py"]