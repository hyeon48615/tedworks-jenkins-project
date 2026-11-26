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

# sshd는 백그라운드에서 동작
# 컨테이너는 프로세스 종료되면 컨테이너도 종료됨
# sshd -D: 포그라운드에서 동작하게 함으로써, 컨테이너가 유지됨

# Docker는 컨테이너의 stdout과 stderr 수집
# /usr/sbin/sshd -e 옵션: stderr 출력 -> docker logs jenkins-node1