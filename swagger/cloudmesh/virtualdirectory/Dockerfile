FROM python:3-onbuild

MAINTAINER Arnav Arnav <aarnav@iu.edu>

RUN apt-get update
RUN apt-get install -qy default-jre
RUN apt-get install build-essential -y -q
RUN apt-get install wget -y

ADD Makefile .
ADD virtual_dir_v0_0_3.yml .

RUN make

EXPOSE 8080

CMD ["make", "run"]
