FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Needed libraries
RUN yum update -y
RUN yum install -y wget xvfb unzip curl

# Install python 3.9
RUN yum -y groupinstall "Development Tools"
RUN yum -y install gcc openssl-devel bzip2-devel libffi-devel
RUN wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
RUN tar zxvf Python-3.9.7.tgz
RUN (cd ./Python-3.9.7 && ./configure)
RUN ls ./Python-3.9.7/
RUN (cd ./Python-3.9.7/ && make)
RUN (cd ./Python-3.9.7/ && make altinstall)
RUN python3.9 --version

# Install pip
RUN python3.9 -m pip install -U pip
RUN python3.9 -m pip install -U setuptools

# Set up the Chrome PPA
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install -y ./google-chrome-stable_current_*.rpm

# Install Chrome
RUN yum install -y google-chrome-stable
RUN google-chrome-stable --version
RUN google-chrome --version

# DO NOT USE YUM AFTER THIS POINT

# Set default
RUN ln -fs /usr/local/bin/python3.9 /usr/bin/python
RUN ln -fs /usr/local/bin/pip3.9 /usr/bin/pip

# Double check versions
RUN python --version
RUN python3.9 --version
RUN pip --version
RUN pip3.9 --version

# Install undetected_chromedriver
RUN pip install undetected_chromedriver

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
