from fastapi import FastAPI, Request
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
async def root():
    return {"message": "DevOps app running new static"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"{request.method} {request.url}")
    response = await call_next(request)
    return response
