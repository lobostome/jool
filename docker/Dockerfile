FROM alpine:3.7

COPY files .

RUN apk update && \
    apk add --no-cache \
      curl \
      python3 \
      git \
      gnupg && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install pipenv && \
    rm -rf /var/cache/apk/*
