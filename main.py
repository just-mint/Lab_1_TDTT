import io
import torch
from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoImageProcessor, TableTransformerForObjectDetection

# 1. KHỞI TẠO MODEL
class TableDetection:
    def __init__(self):
        model_name = "microsoft/table-transformer-detection"
        self.image_processor = AutoImageProcessor.from_pretrained(model_name)
        self.model = TableTransformerForObjectDetection.from_pretrained(model_name)

    def __call__(self, image_bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        inputs = self.image_processor(images=image, return_tensors="pt")
        
        with torch.no_grad():
            outputs = self.model(**inputs)

        target_sizes = torch.tensor([image.size[::-1]])
        results = self.image_processor.post_process_object_detection(
            outputs, threshold=0.5, target_sizes=target_sizes # Ngưỡng 0.5 như đã tinh chỉnh
        )[0]

        detected_tables = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            detected_tables.append({
                "label": self.model.config.id2label[label.item()],
                "confidence": round(score.item(), 3),
                "bounding_box": [round(i, 2) for i in box.tolist()]
            })
        return detected_tables

detector = TableDetection()

# 2. KHỞI TẠO FASTAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {"message": "API Nhận diện bảng biểu (Table Detection) - Đồ án 1"}

@app.get('/health')
async def health():
    return {"status": "ok", "model": "microsoft/table-transformer-detection"}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    try:
        imageBytes = await file.read()
        results = detector(imageBytes)
        return {
            "filename": file.filename,
            "detected_objects": results
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Lỗi khi xử lý ảnh: {str(e)}")