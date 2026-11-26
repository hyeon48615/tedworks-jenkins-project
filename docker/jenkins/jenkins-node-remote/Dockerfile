FROM ubuntu:22.04

RUN apt-get update \
  # Install system packages
  && apt-get install -y \
    python3 \
    openjdk-21-jre \
    openssh-server \
  # Install Python libraries
  && apt-get install -y python3-requests \
  && useradd -m -s /bin/bash jenkins \
  && mkdir -p /run/sshd  /home/jenkins/agent /home/jenkins/.ssh \
  && chown -R jenkins:jenkins /home/jenkins \
  && chmod 700 /home/jenkins/.ssh

RUN mkdir -p /opt/jenkins/data \
  && chown -R jenkins:jenkins /opt/jenkins/data \
  && chmod 750 /opt/jenkins/data

ENTRYPOINT ["/usr/sbin/sshd", "-D", "-e"]