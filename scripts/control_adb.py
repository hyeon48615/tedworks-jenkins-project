# sudo apt update
# sudo apt install -y adb

import subprocess

def adb_command(command, serial=None):
  args = ["adb"]

  if serial:
    args.extend(["-s", serial])

  # 쉘 명령어 문자열을 공백과 따옴표 규칙에 맞는 리스트로 분할함
  args.extend(shlex.split(command)) 

  print(f"명령어: {' '.join(command)}")

  result = subprocess.run(
    args,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace",
    timeout=30
  )

  if result.returncode != 0:
    raise RuntimeError(result.stderr.strip())

  return result.stdout.strip()
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument("-s", "--serial")
  parser.add_argument("-c", "--command", required=True)
  
  args = parser.parse_args()

  try:
    response = adb_command(args.command, args.serial)
    print(response)

  except (RuntimeError, OSError, subprocess.TimeoutExpired) as e:
    print(f"adb 명령어 실행 실패: {e}", file=sys.stderr)
    sys.exit(1)