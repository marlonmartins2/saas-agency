from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from schemas.agency import AgencyCreate, AgencyInDB
from controllers.agency import Agency


router = APIRouter(prefix="/agencies", tags=["Agências"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AgencyCreate)
def create(agency: AgencyCreate):
    payload = AgencyInDB(**agency.model_dump())
    Agency.insert_one(payload.model_dump())

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "Agência criada com sucesso",
            "agency_id": payload.id,
        },
    )

@router.get("/")
def listar():
    agencias = list(Agency.find())
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=agencias,
    )
