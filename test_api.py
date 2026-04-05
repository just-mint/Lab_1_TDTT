import requests
import json

API_URL = "http://127.0.0.1:8000/predict"

image_files = ["test1.jpg", "test2.jpg", "test3.jpg"]

for filename in image_files:
    try:
        with open(filename, "rb") as image_file:
            files = {"file": image_file}
            response = requests.post(API_URL, files=files)
        
        result = response.json()
        print(json.dumps(result, indent=4, ensure_ascii=False))
        print("\n")
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.\n")
    except Exception as e:
        print(f"Lỗi khi gọi API với file {filename}: {str(e)}\n")