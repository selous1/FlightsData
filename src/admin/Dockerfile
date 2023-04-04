FROM condaforge/mambaforge:latest
WORKDIR ./microservice
COPY ../../.config/envs/requirements.txt ./microservice
RUN conda install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]