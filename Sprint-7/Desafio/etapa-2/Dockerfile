FROM amazonlinux:2023

RUN dnf update -y
RUN dnf install -y python3.11 python3.11-pip zip
RUN dnf clean all

# Cria a pasta padrão que a AWS Lambda exige para camadas Python
RUN mkdir -p /root/layer_dir/python

# Instala a lib: requests no package
RUN python3.11 -m pip install numpy==1.26.4 requests pandas -t /root/layer_dir/python

WORKDIR /root/layer_dir
RUN zip -r layer-tmdb-libs.zip .