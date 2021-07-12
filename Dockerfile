FROM python:3.8-slim

COPY . /fastemplate/

WORKDIR /fastemplate

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir .

CMD ["/bin/bash", "entrypoint.sh"]
