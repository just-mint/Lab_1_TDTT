# API Nhận Diện Bảng Biểu (Table Detection)

## 1. Thông tin sinh viên
* **Họ và tên:** Lâm Duy Minh
* **MSSV:** 24120091

## 2. Thông tin mô hình
* **Tên mô hình:** `microsoft/table-transformer-detection`
* **Liên kết Hugging Face:** [Table Transformer (DETR)](https://huggingface.co/microsoft/table-transformer-detection)

## 3. Mô tả chức năng
 API có khả năng nhận diện và trích xuất vị trí các bảng biểu (Table Detection) bên trong hình ảnh tài liệu. API sẽ nhận đầu vào là một file ảnh được người dùng tải lên, sau đó sử dụng mô hình học máy Table Transformer (dựa trên kiến trúc DETR) để phân tích. Kết quả trả về là tọa độ khung bao (bounding box) của các bảng biểu tìm thấy cùng độ tin cậy (confidence score) dưới định dạng chuẩn JSON.

## 4. Hướng dẫn cài đặt thư viện
Yêu cầu hệ thống đã cài đặt Python 3.x.  
Để cài đặt các thư viện cần thiết, chạy lệnh sau trong terminal:
```bash
pip install -r requirements.txt
```
## 5. Hướng dẫn chạy API
Sau khi cài đặt xong các thư viện, khởi động API bằng cách chạy lệnh sau trong terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
API sẽ chạy tại địa chỉ `http://localhost:8000`. 
## 6. Kết quả thử nghiệm
Khi gửi một hình ảnh tài liệu chứa bảng biểu đến API, bạn sẽ nhận được phản hồi JSON với cấu trúc như sau:
```json
{
    "filename": "test1.jpg",
    "detected_objects": [
        {
            "label": "table",
            "confidence": 0.97,
            "bounding_box": [
                197.12,
                248.03,
                518.57,
                581.85
            ]
        }
    ]
}
```
Trong đó:
- `filename`: Tên file ảnh đã được xử lý.
- `detected_objects`: Danh sách các đối tượng được phát hiện, mỗi đối tượng bao gồm:
  - `label`: Nhãn của đối tượng
  - `confidence`: Điểm tin cậy của dự đoán
  - `bounding_box`: Tọa độ của khung bao quanh đối tượng được phát hiện  
## 7. Video demo
https://github.com/user-attachments/assets/f4bb6f1a-bac8-454e-a024-f4bdb59f864b



