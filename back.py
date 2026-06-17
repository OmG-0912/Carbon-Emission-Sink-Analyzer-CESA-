import os
from fastapi import FastAPI, UploadFile, File
from google import genai
from google.genai import types
from pydantic import BaseModel

app = FastAPI()

# Replace with your actual API Key
GEMINI_API_KEY = "AIzaSyDQMkShtwah-Pp4NkWh4malX2Y2sM3XGVY"
client = genai.Client(api_key=GEMINI_API_KEY)

class Medication(BaseModel):
    name: str
    dosage: str
    frequency: str
    
class PrescriptionData(BaseModel):
    patient_name: str | None
    diagnosis: str | None
    medications: list[Medication]
    notes: str | None

@app.post("/test-extract")
async def test_extract(file: UploadFile = File(...)):
    contents = await file.read()
    
    # This configuration forces Gemini to return structured JSON
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(data=contents, mime_type="image/jpeg"),
            "Extract the medical details from this prescription."
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=PrescriptionData,
        ),
    )
    return response.parsed

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
