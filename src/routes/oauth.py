from fastapi import APIRouter, HTTPException, Form

from src.services import create_access_token

router = APIRouter(tags=["Authentication"])



@router.post("/token")
def login(username: str=Form(...), password: str=Form(...)):
    """
    Authenticates a user and generates an access token if the credentials are valid.\n

    Args:\n
        username (str): The username of the user attempting to log in.\n
        password (str): The password of the user attempting to log in.\n

    Returns:\n
        dict: A dictionary containing the access token and token type if authentication is successful.\n

    Raises:\n
        HTTPException: If the provided credentials are invalid, an HTTP 401 Unauthorized exception is raised.\n
    """
    if username == "user" and password == "password":
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


#usage example
# @router.get("/protected_test")
# def protected_route(current_user: dict = Depends(get_current_user)):
#     return {"message": "You have access to this route", "user": current_user}