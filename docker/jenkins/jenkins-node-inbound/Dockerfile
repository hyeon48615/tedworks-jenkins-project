FROM ubuntu:22.04

RUN apt-get update \
  # Install system packages
  && apt-get install -y \
    python3 \
    openjdk-21-jre \
    curl \
  # Install Python libraries
  && apt-get install -y python3-requests \
  && useradd -m -s /bin/bash jenkins \
  && mkdir -p /home/jenkins/agent \
  && chown -R jenkins:jenkins /home/jenkins

RUN mkdir -p /home/jenkins/data \
  && chown -R jenkins:jenkins /home/jenkins/data \
  && chmod 750 /home/jenkins/data

# Configure agent startup
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

USER jenkins

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]