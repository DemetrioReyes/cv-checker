from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from services.pdf_reader import extract_text_from_pdf
from services.analyzer import analyze_cv
from services.job_matcher import JobMatcher

router = APIRouter(prefix="/job-match", tags=["Job Matching"])
templates = Jinja2Templates(directory="templates")
job_matcher = JobMatcher()

@router.post("/analyze/")
async def analyze_job_match(
    request: Request,
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    pdf_bytes = await file.read()
    cv_text = extract_text_from_pdf(pdf_bytes)
    cv_analysis = analyze_cv(cv_text)
    
    job_requirements = job_matcher.analyze_requirements(job_description)
    
    match_results = job_matcher.calculate_match(cv_analysis, job_requirements)
    
    return templates.TemplateResponse(
        "job_match.html",
        {
            "request": request,
            "cv_analysis": cv_analysis,
            "match_results": match_results,
            "job_description": job_description
        }
    ) 