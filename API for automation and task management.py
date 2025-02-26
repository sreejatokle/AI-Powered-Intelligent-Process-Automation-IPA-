from fastapi import FastAPI
import pytesseract
from PIL import Image

app = FastAPI()

# Endpoint for OCR
@app.post("/process-image/")
async def process_image(image_path: str):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return {"extracted_text": text}

# Example of running this FastAPI server
# uvicorn filename:app --reload
