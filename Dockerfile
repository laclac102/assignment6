FROM python:3.8-slim

RUN apt-get update && apt install -y procps g++ && apt-get clean

RUN mkdir -p /opt/analysis/bin

WORKDIR /opt/analysis

COPY bin /opt/analysis/bin

ENV PATH="/opt/analysis/bin:$PATH"

CMD ["bash"]