import settings

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from version import __version__ as version


load_dotenv()

app = FastAPI(
    title="SaaS Agency",
    description="SaaS para agências de viagem nacionais e internacionais",
    version=version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
def health_check():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "message": "API is running",
        },
    )
