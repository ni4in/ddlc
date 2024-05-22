FROM python:3.10
EXPOSE 5001
WORKDIR /app
COPY requirements.txt .
RUN apt update; apt install -y libgl1
RUN pip install -r requirements.txt
COPY . .
CMD [ "python","test.py" ]