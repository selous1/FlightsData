FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

#COPY key.json ./
COPY app.py ./

EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]