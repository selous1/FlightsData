FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/prod-conda-env.yml /app

RUN mamba env create -f prod-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

SHELL ["conda", "run", "-n", "cen16-prod", "/bin/bash", "-c"]

COPY ./src/flights /app
COPY ./src/GRPC /app

EXPOSE 5003
EXPOSE 50051

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cen16-prod", "python", "app.py"]

# How to push to docker hub:
# docker build -t flights:latest -f src/flights/Dockerfile .
# docker tag flights selous1/flights:v1.0
# docker push selous1/flights:v1.0