FROM python:3.10

WORKDIR /app

COPY requirements.txt .

#RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 8080

COPY . .

CMD [ "python", "main.py" ]
