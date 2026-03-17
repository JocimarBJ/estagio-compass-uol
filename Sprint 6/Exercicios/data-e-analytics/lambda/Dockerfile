FROM amazonlinux:2023

RUN dnf update -y
RUN dnf install -y python3.11 python3.11-pip zip
RUN dnf clean all

RUN mkdir -p /root/layer_dir/python
RUN python3.11 -m pip install numpy==1.26.4 pandas -t /root/layer_dir/python

WORKDIR /root/layer_dir
RUN zip -r minha-camada-pandas.zip .