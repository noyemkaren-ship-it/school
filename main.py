from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from api.router import router
import os
from common.utils import MCKO_QUESTIONS
import urllib.parse

app = FastAPI(title="School11_HUB")

app.include_router(router)

templates = Jinja2Templates(directory="templates")

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/api/mcko/{subject}/{class_level}/{variant}")
async def get_mcko_questions(subject: str, class_level: int, variant: int):
    key = f"{subject}_{class_level}_v{variant}"
    if key in MCKO_QUESTIONS:
        return MCKO_QUESTIONS[key]
    raise HTTPException(status_code=404, detail="Вариант не найден")


@app.post("/api/mcko/check")
async def check_mcko_answers(answers: dict):
    variant_key = answers.get("variant_key")
    user_answers = answers.get("answers", {})

    if variant_key not in MCKO_QUESTIONS:
        raise HTTPException(status_code=404, detail="Вариант не найден")

    questions = MCKO_QUESTIONS[variant_key]["questions"]
    score = 0
    results = {}

    for q in questions:
        q_id = str(q["id"])
        user_ans = user_answers.get(q_id, "")
        is_correct = user_ans.lower().strip() == q["answer"].lower().strip()
        if is_correct:
            score += 1
        results[q_id] = is_correct

    total = len(questions)
    grade = 2
    if score >= total - 1:
        grade = 5
    elif score >= total - 2:
        grade = 4
    elif score >= total // 2:
        grade = 3

    return {
        "score": score,
        "total": total,
        "grade": grade,
        "results": results,
        "questions": questions
    }


@app.get("/")
async def home(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    return templates.TemplateResponse("index.html", {"request": request, "user": user})


@app.get("/main")
async def main_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Необходимо войти в систему"})


@app.get("/users")
async def users_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/materials")
async def materials_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("materials.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/materials/add")
async def add_material_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("material_add.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/tests")
async def tests_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("tests.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/test/{test_id}")
async def test_pass_page(request: Request, test_id: int):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("test_pass.html", {
            "request": request,
            "user": user,
            "test_id": test_id
        })
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/test/create")
async def create_test_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("test_create.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/results")
async def results_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("results.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/profile")
async def profile_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("profile.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/mcko")
async def mcko_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    return templates.TemplateResponse("mcko.html", {"request": request, "user": user})


@app.get("/my_scores")
async def my_scores_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("my_scores.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/my_tests")
async def my_tests_page(request: Request):
    raw_surname = request.cookies.get("surname")
    user = urllib.parse.unquote(raw_surname) if raw_surname else None
    if user:
        return templates.TemplateResponse("my_tests.html", {"request": request, "user": user})
    return templates.TemplateResponse("error.html", {"request": request, "error": "Доступ запрещен"})


@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/logout")
async def logout(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie("surname")
    return response


@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "error": "Страница не найдена"
    }, status_code=404)


@app.exception_handler(500)
async def internal_error_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "error": "Внутренняя ошибка сервера"
    }, status_code=500)


@app.get("/error")
async def error_page(request: Request, error: str = ""):
    return templates.TemplateResponse("error.html", {"request": request, "error": error})