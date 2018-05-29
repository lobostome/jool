FROM alpine:edge

COPY files .

RUN apk update && \
    apk add --no-cache \
      curl \
      python3=3.6.4-r1 \
      libgit2=0.27.0-r0 \
      git \
      openssh \
      gnupg && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install pipenv nltk && \
    python3 -m nltk.downloader 'punkt' && \
    rm -rf /var/cache/apk/*
