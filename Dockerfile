FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Disable this for local development
COPY . .

CMD [ "python", "main.py" ]
