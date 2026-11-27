import os
import sys

if __name__ == "__main__":
    folder_name = sys.argv[1]
    file_name = sys.argv[2]
    file_content = sys.argv[3]

    if not folder_name or not file_name:
        raise ValueError("폴더명과 파일명은 비워둘 수 없습니다.")
    
    base_dir = "/home/jenkins/data"

    target = os.path.join(base_dir, folder_name, file_name)
    os.makedirs(os.path.dirname(target), exist_ok=True)

    with open(target, "w", encoding="UTF-8") as f:
        f.write(file_content)