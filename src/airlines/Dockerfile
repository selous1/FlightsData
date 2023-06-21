FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/prod-conda-env.yml /app

RUN mamba env create -f prod-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

SHELL ["conda", "run", "-n", "cen16-prod", "/bin/bash", "-c"]

COPY ./src/airlines /app
COPY ./src/GRPC /app

EXPOSE 5001

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cen16-prod", "python", "app.py"]

# How to push to docker hub
# i dont like
# docker build -t airlines:latest -f src/airlines/Dockerfile .
# docker tag airlines selous1/airlines:v1.0
# docker push selous1/airlines:v1.0