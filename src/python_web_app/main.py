from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from python_web_app.auth.router import router as auth_router
from python_web_app.fast_path_op.router import router as fast_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(fast_router)
"""
this is also possible.
adding prefix and dependencies to the router
when including the router to the app
app.include_router(
    fast_router,
    prefix="/fast-path-op",
    tags=["fast-path-op"],
    dependencies=[Depends(get_current_user)]
)
"""

@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "healthy"}