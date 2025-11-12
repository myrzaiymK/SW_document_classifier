from fastapi import FastAPI, File, UploadFile
from dify_classifier import DocumentClassifier

app = FastAPI(title="Document Type Classifier API")
classifier = DocumentClassifier()


@app.post("/classify")
async def classify_document(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        text = content.decode("latin-1", errors="ignore")

    if not text.strip():
        return {"error": "File is empty or contains no readable text"}

    result = classifier.classify_text(text)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
