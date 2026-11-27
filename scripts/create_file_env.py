import os

if __name__ == "__main__":
    directory = os.environ.get('directory')
    file_name = os.environ.get('file_name')
    file_content = os.environ.get('file_content')

    if not directory or not file_name:
        raise ValueError("폴더명과 파일명은 비워둘 수 없습니다.")
    
    base_dir = "/home/jenkins/data"

    target = os.path.join(base_dir, directory, file_name)

    os.makedirs(os.path.dirname(target), exist_ok=True)

    try:
        with open(target, "x", encoding="UTF-8") as f:
            f.write(file_content)

        print(f"파일 생성 완료: {target}")
    
    except FileExistsError:
        print(f"이미 존재하는 파일입니다.: {target}")