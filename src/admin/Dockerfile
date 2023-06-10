FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/dev-conda-env.yml /app

RUN mamba env create -f dev-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

SHELL ["conda", "run", "-n", "cen16-dev", "/bin/bash", "-c"]


COPY ./src/admin /app

EXPOSE 5000

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "cen16-dev", "python", "microservice/app.py"]

# https://pythonspeed.com/articles/activate-conda-dockerfile/
# Runs with commands
# sudo docker build -t admin:latest -f src/admin/Dockerfile .
# sudo docker run -p 5000:5000 admin:latest
# From project root