#!/bin/bash

set -e # 오류 발생 시 중단

curl -fsSL "${JENKINS_URL%/}/jnlpJars/agent.jar" \
  -o /home/jenkins/agent.jar

exec java -jar /home/jenkins/agent.jar \
  -url "$JENKINS_URL" \
  -secret "$JENKINS_SECRET" \
  -name "$JENKINS_AGENT_NAME" \
  -webSocket \
  -workDir "/home/jenkins/agent"