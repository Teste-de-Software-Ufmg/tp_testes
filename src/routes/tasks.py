from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer

from src.controllers import TaskController
from src.models import TaskBody
from src.services import get_current_user

router = APIRouter(tags=["Tasks"])

task_controller = TaskController()

@router.get("/task/{task_id}", status_code=200)
def get_task(
    task_id: int,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):  
    """
    Retrieve a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.
        credentials (OAuth2AuthorizationCodeBearer): The credentials of the current user, 
            automatically injected by FastAPI's dependency injection system.

    Returns:
        dict: The task data if found.

    Raises:
        HTTPException: If the task is not found or if there is an internal server error.
    """
    try:
        return task_controller.get(task_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.get("/tasks", status_code=200)
def get_all_tasks(credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user)):
    """
    Retrieve all tasks.

    Args:
        -

    Returns:
        dict: The list of tasks.
    
    Raises:
        HTTPException: If there is an HTTP error during task retrieval.\n
        HTTPException: If there is an internal server error.
    """
    try:
        return task_controller.get_all()
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.post("/task/create", status_code=200)
def create_task(
    body: TaskBody,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    """
    Create a new task.

    Args:
        body (TaskBody): The body of the task to be created.\n

    Returns:
        Task: The created task.

    Raises:
        HTTPException: If there is an HTTP error during task creation.\n
        HTTPException: If there is an internal server error.
    """

    try:
        return task_controller.create(body)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.post("/task/update/{task_id}", status_code=200)
def update_task(
    task_id: int,
    body: TaskBody,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    """
    Update an existing task.

    Args:
        task_id (int): The ID of the task to update.\n
        body (TaskBody): The new data for the task.\n

    Returns:
        The updated task.

    Raises:
        HTTPException: If an HTTP error occurs.\n
        HTTPException: If an internal server error occurs.\n
    """

    try:
        return task_controller.update(task_id, body)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.post("/task/vinculate", status_code=200)
def vinculate_task(
    task_id: int,
    person_id: int,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    """
    Endpoint to vinculate a task to a person.

    Args:
        task_id (int): The ID of the task to be vinculared.\n
        person_id (int): The ID of the person to whom the task will be vinculared.

    Returns:
        dict: The result of the vinculation operation.

    Raises:
        HTTPException: If an HTTP error occurs during the vinculation process.\n
        HTTPException: If an internal server error occurs.
    """
    try:
        return task_controller.vinculate(task_id, person_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.post("/task/conclude/{task_id}", status_code=200)
def conclude_task(
    task_id: int,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    """
    Conclude a task by its ID.

    Args:
        task_id (int): The ID of the task to be concluded.\n

    Returns:
        The result of the task conclusion operation.

    Raises:
        HTTPException: If an HTTP error occurs during the conclusion process.\n
        HTTPException: If an internal server error occurs.\n
    """

    try:
        return task_controller.conclude(task_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e

@router.delete("/task/delete/{task_id}", status_code=200)
def delete_task(
    task_id: int,
    credentials: OAuth2AuthorizationCodeBearer = Depends(get_current_user),
):
    """
    Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to be deleted.\n

    Returns:
        The result of the task deletion operation.

    Raises:
        HTTPException: If an HTTP error occurs during the deletion process.\n
        HTTPException: If an internal server error occurs.\n
    """

    try:
        return task_controller.delete(task_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        ) from e
