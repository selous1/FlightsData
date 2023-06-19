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
# docker build -t admin:latest -f src/admin/Dockerfile .
# docker tag admin santig007/cnproject:admin1.0
# docker push santig007/cnproject:admin1.0

# hopefully pushes to container registry

# Command to test cloud build:
# curl -X POST -H "application/json" "https://cloudbuild.googleapis.com/v1/projects/cnproject-381016/triggers/trigger-test:webhook?key=AIzaSyDx6bIBtpbGl3tkF7RqySY543YAwJVxldw&secret=GdtV2NNLvAlh_GN-mBCecH90CtX7HNOM" -d "{}"
# https://console.cloud.google.com/cloud-build/triggers;region=global?hl=pt-pt&project=cnproject-381016