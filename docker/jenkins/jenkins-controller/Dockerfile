From jenkins/jenkins:latest

USER root

RUN apt-get update \
  # Install system packages
  && apt-get install -y python3 \
  # Install Python libraries
  && apt-get install -y python3-requests

RUN mkdir -p /opt/jenkins/data \
  && chown jenkins:jenkins /opt/jenkins/data \
  && chmod 750 /opt/jenkins/data

USER jenkins