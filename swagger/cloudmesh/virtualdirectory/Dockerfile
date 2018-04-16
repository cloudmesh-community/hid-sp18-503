FROM mongo
#FROM python:3-onbuild

MAINTAINER Arnav Arnav <aarnav@iu.edu>

#RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update

#RUN apt-install -y apt-utils

RUN apt-get install build-essential -y -q

RUN apt-get install wget -y

# install python 3
RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -qy default-jre

#RUN \
#  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
#  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist \
#  10gen' > /etc/apt/sources.list.d/mongodb.list && \
#  apt-get update && \
#  apt-get install -y mongodb-org && \

ADD Makefile .
ADD test_build .
ADD virtual_dir_v0_0_3.yml .

RUN make -f test_build install

VOLUME ["~/cloudmesh/data/db"]
CMD ["make", "run"]

#CMD ["bash"]