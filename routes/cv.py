from fastapi import APIRouter, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from services.pdf_reader import extract_text_from_pdf
from services.analyzer import analyze_cv

router = APIRouter(prefix="/cv", tags=["CV Analysis"])
templates = Jinja2Templates(directory="templates")

@router.post("/upload/")
async def upload_cv(request: Request, file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    text = extract_text_from_pdf(pdf_bytes)
    result = analyze_cv(text)
    
    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "filename": file.filename,
            "result": result
        }
    )
