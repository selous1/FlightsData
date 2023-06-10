# https://pythonspeed.com/articles/activate-conda-dockerfile/
#
# How to run (from project root directory):
#
# > sudo docker build -t ranking:latest -f src/ranking/Dockerfile .
# > sudo docker run --name ranking --rm -p 5000:5000 ranking:latest
#
# How to push to docker hub:
# docker build -t ranking:latest -f src/ranking/Dockerfile .
# docker tag ranking selous1/ranking:<version>
# docker push selous1/ranking:<version>

FROM condaforge/mambaforge:latest

WORKDIR /app

COPY .config/envs/prod-conda-env.yml /app

RUN mamba env create -f prod-conda-env.yml
RUN mamba init bash
RUN conda config --set auto_activate_base false

SHELL ["conda", "run", "-n", "cen16", "/bin/bash", "-c"]

COPY ./src/ranking /app

EXPOSE 5000

ENTRYPOINT ["docker", "pull", "condaforge/mambaforge:latest", "&&", "conda", "run", "--no-capture-output", "-n", "cen16", "python", "microservice/app.py"]


