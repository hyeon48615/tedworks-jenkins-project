From jenkins/jenkins:latest

USER root

RUN apt-get update \
  # Install system packages
  && apt-get install -y python3 \
  # Install Python libraries
  && apt-get install -y python3-requests

RUN mkdir -p /var/jenkins/data \
  && chown jenkins:jenkins /var/jenkins/data \
  && chmod 750 /var/jenkins/data

USER jenkins