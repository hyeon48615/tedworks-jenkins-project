import os
import argparse
import requests

JENKINS_URL = "http://172.30.1.77:8088"
JENKINS_USER = "admin"
JENKINS_TOKEN = os.environ["JENKINS_TOKEN"]

JOB_NAME = "4. create file(node)"

url = f"{JENKINS_URL}/job/{JOB_NAME}/buildWithParameters"

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory")
parser.add_argument("-n", "--name")
parser.add_argument("-c", "--content")

args = parser.parse_args()

params = {
  "FOLDER_NAME": args.directory,
  "FILE_NAME": args.name,
  "FILE_CONTENT": args.content
}

response = requests.post(
  url,
  auth=(JENKINS_USER, JENKINS_TOKEN),
  data=params,
)

if response.status_code == 201:
  print("Jenkins 빌드 요청 성공")
else:
  print("Jenkins 빌드 요청 실패")
  print(f"status: {response.status_code}, message: {response.text}")