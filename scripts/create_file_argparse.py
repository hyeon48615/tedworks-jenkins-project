import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory")
    parser.add_argument("-n", "--name")
    parser.add_argument("-c", "--content")

    args = parser.parse_args()

    if not args.directory or not args.name:
        raise ValueError("폴더명과 파일명은 비워둘 수 없습니다.")
    
    base_dir = "/home/jenkins/data"

    target = os.path.join(base_dir, args.directory, args.name)

    os.makedirs(os.path.dirname(target), exist_ok=True)

    try:
        with open(target, "x", encoding="UTF-8") as f:
            f.write(args.content)

        print(f"파일 생성 완료: {target}")
    
    except FileExistsError:
        print(f"이미 존재하는 파일입니다.: {target}")