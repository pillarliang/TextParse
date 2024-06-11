# FROM nvidia/cuda:12.1.0-devel-ubuntu22.04 as base
FROM python:3.8

RUN chmod 1777 /tmp
# RUN apt-get update
# RUN apt-get install -y python3 git python3-pip
# RUN ln -s /usr/bin/python3 /usr/bin/python

# RUN apt-get install vim -y
WORKDIR /workspace/api

# install build and runtime dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /workspace/api

EXPOSE 8006

ENV HF_ENDPOINT="https://hf-mirror.com"
ENV HUGGING_FACE_HUB_TOKEN="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"

# Command to run the application
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8006"]