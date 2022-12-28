FROM python:3.11-slim

LABEL Maintainer="mastergowen@gmail.com"

ARG SSEKER_REPOSITORY={{ SSEKER_REPOSITORY }}
ARG SSEKER_VERSION={{ SSEKER_VERSION }}

RUN apt-get update \
    && apt-get install -y --no-install-recommends git curl libcurl4-openssl-dev \
               libssl-dev libc6 libc6-dev gcc g++\
    && pip install --upgrade --no-cache-dir pip \
    && apt-get auto-remove -y && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/sseker && git clone $SSEKER_REPOSITORY --branch $SSEKER_VERSION --single-branch /app/sseker
WORKDIR /app/sseker

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]
#CMD ["tail", "-f", "/dev/null"]