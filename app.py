import io
import os
import base64
from urllib.parse import quote

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import qrcode

app = FastAPI(title="Fixed GitHub QRCode Demo")
templates = Jinja2Templates(directory="templates")

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "mosguo")


def github_profile_url(username: str) -> str:
    return f"https://github.com/{quote(username)}"


def make_qr_data_uri(text: str) -> str:
    img = qrcode.make(text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    username = GITHUB_USERNAME
    target_url = github_profile_url(username)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "username": username,
            "target_url": target_url,
        },
    )


@app.get("/qrcode", response_class=HTMLResponse)
async def show_qrcode(request: Request):
    username = GITHUB_USERNAME
    target_url = github_profile_url(username)
    qr_data_uri = make_qr_data_uri(target_url)
    return templates.TemplateResponse(
        "qrcode.html",
        {
            "request": request,
            "username": username,
            "target_url": target_url,
            "qr_data_uri": qr_data_uri,
        },
    )
