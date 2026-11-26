import os
import json
import requests

# Jenkins 기본 환경변수
JENKINS_URL = os.environ["JENKINS_URL"]
JENKINS_BUILD_NO = os.environ["BUILD_NUMBER"]
# Jenkins Credential
JENKINS_USER = os.environ["JENKINS_USER"]
JENKINS_TOKEN = os.environ["JENKINS_TOKEN"]
JENKINS_NODE = os.environ["jenkins_node"]

url = f"{JENKINS_URL}/manage/computer/{JENKINS_NODE}/api/json"

response = requests.get(url, auth=(JENKINS_USER, JENKINS_TOKEN))

if response.status_code == 200:
  print("Jenkins Node 조회 성공")
else:
  print("Jenkins Node 조회 실패")
  print(f"status: {response.status_code}, message: {response.text}")
  response.raise_for_status()

node = response.json()

result = {
  "node": {
    "name": node.get("displayName"),
    "labels": [
      label["name"] for label in node.get("assignedLabels", [])
    ],
    "idle": node.get("idle"),
    "executors": node.get("numExecutors", 0),
    "offline": node.get("offline")
  }
}

base_dir = "/opt/jenkins/data"
file_name = f"node_info_{JENKINS_BUILD_NO}.json"

target = os.path.join(base_dir, file_name)

with open(target, "w", encoding="UTF-8") as f:
  json.dump(result, f, ensure_ascii=False)

print(f"Jenkins Node 정보 저장 성공: {target}")