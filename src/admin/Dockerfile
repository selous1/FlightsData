FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/dev-conda-env.yml /app

RUN mamba env create -f dev-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

SHELL ["conda", "run", "-n", "cen16-dev", "/bin/bash", "-c"]

COPY ./src/admin /app

EXPOSE 5005

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cen16-dev", "python", "app.py"]

# https://pythonspeed.com/articles/activate-conda-dockerfile/
# Runs with commands
# sudo docker build -t admin:latest -f src/admin/Dockerfile .
# sudo docker run -p 5000:5000 admin:latest
# From project root
# Push to Docker Hub
# How to push to docker hub:1
# docker build -t admin:latest -f src/admin/Dockerfile .
# docker tag admin santig007/cnproject:admin1.0
# docker push santig007/cnproject:admin1.0