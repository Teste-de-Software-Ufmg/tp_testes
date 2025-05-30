from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

from src.controllers import PersonController
from src.models import PersonBody
from src.services import get_current_user

router = APIRouter(tags=["persons"])

person_controller = PersonController()

@router.get("/person/{person_id}", status_code=200)
def get_person(
    person_id: int,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    try:
        return person_controller.get(person_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.post("/person/create", status_code=200)
def create_person(
    body: PersonBody,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    try:
        return person_controller.create(body)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.post("/person/update/{person_id}", status_code=200)
def update_person(
    person_id: int,
    body: PersonBody,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    try:
        return person_controller.update(person_id, body)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.delete("/person/delete/{person_id}", status_code=200)
def delete_person(
    person_id: int,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    try:
        return person_controller.delete(person_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e