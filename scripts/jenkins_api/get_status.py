import os
import requests

JENKINS_URL = "http://172.30.1.77:8088"
JENKINS_USER = "admin"
JENKINS_TOKEN = os.environ["JENKINS_TOKEN"]

JOB_NAME = "4. create file(node)"

url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"

response = requests.get(url, auth=(JENKINS_USER, JENKINS_TOKEN))

if response.status_code == 200:
  data = response.json()
  print(f"빌드 번호: {data.get('number')}")
  print(f"빌드 결과: {data.get('result')}")
else:
  print("Jenkins 상태 조회 실패")
  print(f"status: {response.status_code}, message: {response.text}")