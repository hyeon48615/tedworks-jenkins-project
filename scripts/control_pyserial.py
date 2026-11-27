# https://www.pyserial.com/docs/reading-data
# pip install uv
# uv add pyserial

import serial
import time
import argparse

# 1. 시리얼 포트 설정
# python3 -m serial.tools.list_ports -v: 연결된 시리얼 포트 확인
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", required=True)
parser.add_argument("-s", "--speed", required=True)
args = parser.parse_args()

# 2. 포트가 열려 있는지 확인
# if serial.is_open:
# serial.cloas() -> with문이 resource 자동 해제
try:
  with serial.Serial(
    port=args.port,
    baudrate=args.speed,
    timeout=1
  ) as board:
    print(f"[{ser.name}] 포트와 성공적으로 연결되었습니다.")

    while True:
      command = input("> ")

      if (command == "exit"):
        break
      
      # 3. 데이터 쓰기 (서버 -> 보드)
      board.write((command + "\r\n").encode('utf-8'))
      board.flush()
      
      time.sleep(1)

      # 4. 데이터 읽기 (보드 -> 서버)
      # 바이트 -> 문자열 변환(디코딩) 중 오류 발생 시, 대체 문자로 치환
      response = board.read_all().decode("utf-8", errors="replace")
      print(response)

except serial.SerialException as e:
  print(f"시리얼 통신오류가 발생했습니다.: {e}")
  raise SystemExit(1)

except KeyboardInterrupt:
  print(f"프로그램이 종료되었습니다.")