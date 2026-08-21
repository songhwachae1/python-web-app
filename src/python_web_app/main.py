from fastapi import FastAPI

from python_web_app.auth.router import router as auth_router
from python_web_app.fast_path_op.router import router as fast_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(fast_router)

@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "healthy"}