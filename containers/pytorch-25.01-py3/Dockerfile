ARG BASE_TAG=25.01-py3
FROM nvcr.io/nvidia/pytorch:$BASE_TAG

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3-venv && apt-get clean && rm -rf /var/lib/apt/lists/*
