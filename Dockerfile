FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Packages
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    gnupg \
    software-properties-common \
    python3 \
    python3-pip \
    ssh \
    git \
    && rm -rf /var/lib/apt/lists/*

# Config
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8

# Ansible
RUN pip3 install ansible

# Terraform
ARG TERRAFORM_VERSION=1.6.6
RUN curl -fsSL https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o terraform.zip && \
    unzip terraform.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform.zip

WORKDIR /workspace

CMD [ "bash" ]
