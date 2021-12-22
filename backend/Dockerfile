  
FROM python:3.8


RUN apt update -y \
    && apt install nginx -y \
    && apt-get install software-properties-common -y \
    && apt-add-repository -r ppa:certbot/certbot \
    # && add-apt-repository ppa:certbot/certbot -y \
    && apt-get update -y \
    && apt-get install python3-certbot-nginx -y \
    && apt-get clean


RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
