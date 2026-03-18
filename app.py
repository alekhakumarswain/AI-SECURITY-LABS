import os
import yaml
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DETAILS_DIR = os.path.join(BASE_DIR, "details")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

def load_lab_data(filename):
    filepath = os.path.join(DETAILS_DIR, filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError:
            return None

def get_all_courses():
    courses = []
    if not os.path.exists(DETAILS_DIR):
        return courses
    for filename in os.listdir(DETAILS_DIR):
        if filename.endswith(".yaml"):
            data = load_lab_data(filename)
            if data:
                # Add extra course-related metadata if not present
                if "id" not in data:
                    data["id"] = filename.replace(".yaml", "")
                courses.append(data)
    return courses

# API Endpoints
@app.get("/api/courses")
async def api_get_courses():
    courses = get_all_courses()
    return [{"id": c.get("id"), "title": c.get("title"), "category": c.get("category")} for c in courses]

@app.get("/api/course/{course_id}")
async def api_get_course(course_id: str):
    courses = get_all_courses()
    for course in courses:
        if course.get("id") == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

# Server-side Rendered Page Routes
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/courses")
def read_courses_page(request: Request):
    courses = get_all_courses()
    return templates.TemplateResponse("learn.html", {
        "request": request, 
        "courses": courses,
        "selected_course": None
    })

@app.get("/course/{course_id}")
def read_course_detail(request: Request, course_id: str):
    courses = get_all_courses()
    selected_course = next((c for c in courses if c.get("id") == course_id), None)
    if not selected_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return templates.TemplateResponse("learn.html", {
        "request": request,
        "courses": courses,
        "selected_course": selected_course
    })

@app.get("/labs")
def read_labs_page(request: Request):
    courses = get_all_courses()
    return templates.TemplateResponse("labs.html", {
        "request": request,
        "labs": courses,
        "selected_lab": None
    })

@app.get("/labs/{lab_id}")
def read_lab_detail(request: Request, lab_id: str):
    courses = get_all_courses()
    selected_lab = next((c for c in courses if c.get("id") == lab_id), None)
    if not selected_lab:
        raise HTTPException(status_code=404, detail="Lab not found")
    return templates.TemplateResponse("labs.html", {
        "request": request,
        "labs": courses,
        "selected_lab": selected_lab
    })


@app.get("/googlecd7dfb82e8598cb2.html")
async def google_verification():
    return FileResponse(os.path.join(BASE_DIR, "templates", "googlecd7dfb82e8598cb2.html"))

@app.get("/robots.txt")
async def robots():
    content = "User-agent: *\nAllow: /\nSitemap: https://ai-security-labs.vercel.app/sitemap.xml"
    return Response(content=content, media_type="text/plain")

@app.get("/sitemap.xml")
async def sitemap():
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://ai-security-labs.vercel.app/</loc><priority>1.0</priority></url>
    <url><loc>https://ai-security-labs.vercel.app/courses</loc><priority>0.8</priority></url>
    <url><loc>https://ai-security-labs.vercel.app/labs</loc><priority>0.8</priority></url>
</urlset>"""
    return Response(content=content, media_type="application/xml")

@app.get("/manifest.json")
async def manifest():
    return FileResponse(os.path.join(BASE_DIR, "static", "manifest.json"))

# Mount static files
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
