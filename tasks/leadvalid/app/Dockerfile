FROM alpine

RUN apk add --no-cache python3 && python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    apk add --no-cache build-base python3-dev && \
    apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev linux-headers openssl-dev

COPY requirements.txt /
RUN pip install -r /requirements.txt --no-cache-dir && apk del .build-deps
RUN find / -type f -name *config.py -exec sed -i s/safe_load/load/g {} +

VOLUME ["/app"]

USER nobody

WORKDIR /app
CMD ["uwsgi", "--http", "0.0.0.0:8180", "--wsgi-file", "./app.py", "--callable", "app"]
